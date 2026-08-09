from django.shortcuts import render

from .models import (
    Experience,
    Event,
    Talent,
    CollectionItem,
)


def home(request):
    context = {
        "events": Event.objects.filter(available=True)[:3],
        "experiences": Experience.objects.filter(available=True)[:3],
        "talents": Talent.objects.filter(available=True)[:3],
        "collection": CollectionItem.objects.filter(available=True),
    }

    return render(request, "hub/home.html", context)


def about(request):
    return render(request, "hub/about.html")


def contact(request):
    return render(request, "hub/contact.html")


def booking(request):
    talents = Talent.objects.filter(available=True)
    experiences = Experience.objects.filter(available=True)
    events = Event.objects.filter(available=True)

    context = {
        "talents": talents,
        "experiences": experiences,
        "events": events,
    }

    return render(request, "hub/booking.html", context)



def events(request):
    events = Event.objects.filter(available=True)
    return render(request, "hub/events.html", {
        "events": events
    })


def experiences(request):
    experiences = Experience.objects.filter(available=True)
    return render(request, "hub/experiences.html", {
        "experiences": experiences
    })


def collections(request):
    collection = CollectionItem.objects.filter(available=True)
    return render(
        request,
        "hub/collections.html",
        {"collection": collection},
    )