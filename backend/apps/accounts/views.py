from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from .models import User, PanelOTP
from .serializers import (
    UserSerializer,
    PanelOTPSendSerializer,
    PanelOTPCheckSerializer,
)

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    Admin-only CRUD for users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

@api_view(['POST'])
@permission_classes([AllowAny])
def send_panel_otp(request):
    """
    POST /auth/panel/sent-otp
    """
    serializer = PanelOTPSendSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    phone = serializer.validated_data['phone']
    user, _ = User.objects.get_or_create(phone=phone)

    otp = PanelOTP.generate_otp(user)
    # --- SMS stub ---
    print(f"[SMS-STUB] OTP to {phone}: {otp.code}")

    return Response({"detail": "OTP sent"}, status=status.HTTP_201_CREATED)

@api_view(["POST"])
@permission_classes([AllowAny])
def check_panel_otp(request):
    """
    POST /auth/panel/check-otp
    """
    serializer = PanelOTPCheckSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.validated_data["tokens"], status=status.HTTP_200_OK)