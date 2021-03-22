from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = ["User"]


class User(AbstractUser):
    telegram_auth_uuid = models.UUIDField(_("Telegram auth UUID"), default=uuid4)
    telegram_chat_id = models.PositiveIntegerField(_("Telegram chat ID"), null=True, blank=True)

    class Meta:
        app_label = "users"
