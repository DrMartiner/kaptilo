import random
import string

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

__all__ = ["Link"]


def get_short_link_uuid() -> str:
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))


class Link(models.Model):
    uuid = models.CharField(_("Uniq ID"), max_length=8, primary_key=True, default=get_short_link_uuid)
    user = models.ForeignKey(User, models.CASCADE, verbose_name=_("User"))
    original_link = models.URLField(_("Link"), max_length=1024)

    created = models.DateTimeField("Creation date", auto_now_add=True)

    def __str__(self):
        return f"Link {self.short_url} of UserID={self.user.pk}"

    class Meta:
        app_label = "link"
        ordering = ["user", "created"]

    @property
    def short_url(self) -> str:
        return f"{settings.BASE_URL}{self.uuid}"


class Visit(models.Model):
    link = models.ForeignKey("Link", models.CASCADE)
    visitor_data = models.JSONField(_("Visitor data"), default=dict, null=True, blank=True)
    count = models.IntegerField(_("Visited count"), default=0)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "link"
        ordering = ["created"]
