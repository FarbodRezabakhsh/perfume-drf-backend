from .models import User, PanelOTP
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'email', 'is_active', 'is_staff', 'date_joined']
        read_only_fields = ['id', 'date_joined']

class PanelOTPSendSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11)

class PanelOTPCheckSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11)
    code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        phone, code = attrs['phone'], attrs['code']
        try:
            user = User.objects.get(phone=phone)
            otp = (
                user.otps.filter(code=code, is_used=False, expires_at__gt=timezone.now()).latest('created_at')
            )
        except (User.DoesNotExist, PanelOTP.DoesNotExist):
            raise serializers.ValidationError("Invalid phone or code")
        
        otp.is_used = True
        otp.save()

        refresh = RefreshToken.for_user(user)
        attrs['tokens'] = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        
        return attrs