from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, send_panel_otp, check_panel_otp
from django.http import JsonResponse

router = DefaultRouter()
router.register(r"user", UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/panel/sent-otp", send_panel_otp),
    path("auth/panel/check-otp", check_panel_otp),
]