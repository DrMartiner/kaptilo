from rest_framework import serializers

from apps.link import models

__all__ = ["LinkCreateSerializer", "LinkListSerializer", "LinkRetrieveSerializer"]


class LinkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Link
        fields = "__all__"


class LinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Link
        fields = "__all__"


class VisitRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visit
        fields = ["visitor_data", "real_ip", "created"]


class LinkRetrieveSerializer(serializers.ModelSerializer):
    visits = serializers.SerializerMethodField(source="get_visits")

    def get_visits(self, obj: models.Link) -> list[dict]:
        return VisitRetrieveSerializer(obj.visit_set.all(), many=True).data

    class Meta:
        model = models.Link
        fields = ["uuid", "original_link", "visited_count", "created", "visits"]
