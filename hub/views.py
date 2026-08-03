from django.shortcuts import render, redirect
from .models import Experience, Event, Travel, Booking


def home(request):
    return render(request, "hub/home.html")


def about(request):
    return render(request, "hub/about.html")


def experiences(request):
    experiences = Experience.objects.all()
    return render(
        request,
        "hub/experiences.html",
        {"experiences": experiences}
    )


def events(request):
    events = Event.objects.all()
    return render(
        request,
        "hub/events.html",
        {"events": events}
    )


def travel(request):
    travels = Travel.objects.all()
    return render(
        request,
        "hub/travel.html",
        {"travels": travels}
    )


def contact(request):
    return render(request, "hub/contact.html")


def booking(request):
    experiences = Experience.objects.all()
    events = Event.objects.all()
    travels = Travel.objects.all()

    if request.method == "POST":
        Booking.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            experience_id=request.POST.get("experience") or None,
            event_id=request.POST.get("event") or None,
            travel_id=request.POST.get("travel") or None,
        )

        return render(
            request,
            "hub/booking.html",
            {
                "experiences": experiences,
                "events": events,
                "travels": travels,
                "success": "Your booking has been submitted successfully!"
            }
        )

    return render(
        request,
        "hub/booking.html",
        {
            "experiences": experiences,
            "events": events,
            "travels": travels,
        }
    )