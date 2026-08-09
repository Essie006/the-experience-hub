from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("events/", views.events, name="events"),
    path("experiences/", views.experiences, name="experiences"),
    path("booking/", views.booking, name="booking"),
    path("collections/", views.collections, name="collections"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]