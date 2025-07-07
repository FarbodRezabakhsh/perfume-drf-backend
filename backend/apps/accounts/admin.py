from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User, PanelOTP

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display  = ("phone", "email", "is_staff", "is_superuser")
    search_fields = ("phone", "email")
    fieldsets = (
        (None, {"fields": ("phone", "password")}),
        ("Personal info", {"fields": ("email",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups")}),
        ("Dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("phone", "password1", "password2"),
        }),
    )
    ordering = ("phone",)

admin.site.register(PanelOTP)
