from django.urls import reverse
from django_dynamic_fixture import G

import requests_mock

from apps.common.base_test import BaseTest
from apps.link.models import Link


class OriginalLinkRedirectTest(BaseTest):
    original_link = "http://example.com"

    def test_succeed(self):
        link: Link = G(Link, original_link=self.original_link)

        with requests_mock.Mocker() as m:
            m.get(self.original_link)
            url: str = reverse("original-link-redirect", args=[link.uuid])
            response = self.client.get(url)

        self.assertEquals(response.status_code, 302)
