from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from apps.link.views import OriginalLinkRedirectView

admin.site.site_header = "Kaptilo"
admin.site.site_title = "Kaptilo"
admin.site.index_title = "Welcome to Kaptilo admin-panel"

urlpatterns = [
    path('<str:uuid>/', OriginalLinkRedirectView.as_view(), name='original-link-redirect'),
    path("api/v1/", include(("apps.api.urls", "apps.api"), namespace="api_v1")),
    path("admin/super-sec/", admin.site.urls),
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
