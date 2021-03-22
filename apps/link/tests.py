from django.conf import settings
from django.urls import reverse

from django_dynamic_fixture import G

from apps.common.base_test import BaseTest
from apps.link.models import Link, Visit


class OriginalLinkRedirectTest(BaseTest):
    original_link = "http://example.com"

    def test_succeed(self):
        link: Link = G(Link, original_link=self.original_link)

        url: str = reverse("original-link-redirect", args=[link.uuid])
        response = self.client.get(url)

        self.assertEquals(response.status_code, 302)

        link.refresh_from_db()
        self.assertEquals(link.visited_count, 1)

        count: int = Visit.objects.count()
        self.assertEquals(count, 1)

        visit: Visit = Visit.objects.first()
        self.assertEquals(visit.link.pk, link.pk)

    def test_over_visitors_count(self):
        link: Link = G(
            Link, original_link=self.original_link, visited_count=settings.MAX_VISITED_COUNT + 100,
        )

        url: str = reverse("original-link-redirect", args=[link.uuid])
        response = self.client.get(url)

        self.assertEquals(response.status_code, 302)

        link.refresh_from_db()
        self.assertEquals(link.visited_count, settings.MAX_VISITED_COUNT + 100)

        count: int = Visit.objects.count()
        self.assertEquals(count, 0)
