import requests
from django.conf import settings
from django.db import transaction
from django.db.models import F
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from ipware import get_client_ip

from apps.link.models import Link, Visit

__all__ = ["OriginalLinkRedirectView"]


class OriginalLinkRedirectView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        link: Link = get_object_or_404(Link, pk=kwargs['uuid'])

        with transaction.atomic():
            if link.visited_count <= settings.MAX_VISITED_COUNT:
                real_ip, is_routable = get_client_ip(self.request)
                response = requests.get(f"https://ipinfo.io/{real_ip}?token={settings.IPINFO_TOKEN}")

                Visit.objects.create(link=link, visitor_data=response.json(), real_ip=real_ip)

                Link.objects.filter(uuid=kwargs['uuid']).update(visited_count=F("visited_count") + 1)

        return link.original_link
