from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from hub.views import (
    home,
    about,
    experiences,
    events,
    travel,
    contact,
    booking,
)


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),
    path("about/", about, name="about"),
    path("experiences/", experiences, name="experiences"),
    path("events/", events, name="events"),
    path("travel/", travel, name="travel"),
    path("contact/", contact, name="contact"),
    path("booking/", booking, name="booking"),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )