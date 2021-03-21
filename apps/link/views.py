from django.conf import settings
from django.db import transaction, IntegrityError
from django.db.models import F, When, Case, Q
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView

from apps.link.models import Link, Visit

__all__ = ["OriginalLinkRedirectView"]


class OriginalLinkRedirectView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        link: Link = get_object_or_404(Link, pk=kwargs['uuid'])

        with transaction.atomic():
            conditions = Q(uuid=kwargs['uuid']) & Q(visited_count__lte=settings.MAX_VISITED_COUNT)
            try:
                updated_count = Link.objects.update(visited_count=Case(When(conditions, F("visited_count") + 1), default=F("visited_count")))
            except IntegrityError as e:
                updated_count = 0
            except Exception as e:
                raise e

        if updated_count > 0:
            # TODO: to save the user data
            Visit.objects.create(link=link, visitor_data={})

        return link.original_link
