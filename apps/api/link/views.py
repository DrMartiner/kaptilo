import logging

from rest_framework import viewsets

from apps.link import models

from apps.api.views import SerializerViewSetMixin
from . import serializers
from .permissions import LinkPermission

__all__ = ["LinkViewSet"]


logger = logging.getLogger("django.requests")


class LinkViewSet(SerializerViewSetMixin, viewsets.ModelViewSet):
    http_method_names = ["post", "get"]
    queryset = models.Link.objects.all()
    serializer_class_map = {
        'create': serializers.LinkCreateSerializer,
        'list': serializers.LinkListSerializer,
        'retrieve': serializers.LinkRetrieveSerializer,
    }
    permission_classes = [LinkPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return super(LinkViewSet, self).get_queryset().filter(user=self.request.user)
