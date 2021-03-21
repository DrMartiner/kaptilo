from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView

from apps.link.models import Link

__all__ = ["OriginalLinkRedirectView"]


class OriginalLinkRedirectView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        link: Link = get_object_or_404(Link, pk=kwargs['uuid'])

        # TODO: to save the user data

        return link.original_link
