from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from src.users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Admin configuration for the custom User model.
    """
    pass