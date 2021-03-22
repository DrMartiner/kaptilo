from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from . import models


@admin.register(models.User)
class UserAdmin(UserAdmin):
    list_display = ["username", "is_staff"]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (_("Telegram"), {"fields": ("telegram_auth_uuid", "telegram_chat_id")}),
        (
            _("Permissions"),
            {"fields": ("role", "is_active", "is_staff", "is_superuser", "groups", "user_permissions",)},
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
