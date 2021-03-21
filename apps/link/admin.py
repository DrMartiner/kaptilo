from django.contrib import admin
from . import models


class VisitInlineAdmin(admin.StackedInline):
    model = models.Visit
    extra = 0

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.Link)
class LinkAdmin(admin.ModelAdmin):
    inlines = [VisitInlineAdmin]
    list_display = ["uuid", "visited_count", "created"]
    list_filter = ["created"]
    search_fields = ["uuid", "original_link"]

    def visited_count(self, obj: models.Link) -> int:
        return models.Visit.objects.filter(link=obj).count()


@admin.register(models.Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ["id", "link", "created"]
    list_filter = ["created"]
    search_fields = ["link__uuid", "link__original_link"]
