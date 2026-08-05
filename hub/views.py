from django.shortcuts import render

from .models import (
    Experience,
    Event,
    Talent,
    Booking,
    EventSubmission,
    ExperienceSubmission,
)


def home(request):
    return render(request, "hub/home.html")


def about(request):
    return render(request, "hub/about.html")


def experiences(request):
    experiences = Experience.objects.filter(
        available=True
    )

    return render(
        request,
        "hub/experiences.html",
        {
            "experiences": experiences,
        },
    )


def events(request):
    events = Event.objects.filter(
        available=True
    )

    return render(
        request,
        "hub/events.html",
        {
            "events": events,
        },
    )


def contact(request):
    return render(
        request,
        "hub/contact.html"
    )


def booking(request):
    experiences = Experience.objects.filter(
        available=True
    )

    events = Event.objects.filter(
        available=True
    )

    talents = Talent.objects.filter(
        available=True
    )

    if request.method == "POST":

        Booking.objects.create(
            name=request.POST.get(
                "name",
                ""
            ).strip(),

            email=request.POST.get(
                "email",
                ""
            ).strip(),

            phone=request.POST.get(
                "phone",
                ""
            ).strip(),

            talent_id=(
                request.POST.get("talent")
                or None
            ),

            talent_custom=request.POST.get(
                "talent_custom",
                ""
            ).strip(),

            experience_id=(
                request.POST.get("experience")
                or None
            ),

            experience_custom=request.POST.get(
                "experience_custom",
                ""
            ).strip(),

            event_id=(
                request.POST.get("event")
                or None
            ),

            event_custom=request.POST.get(
                "event_custom",
                ""
            ).strip(),
        )

        return render(
            request,
            "hub/booking.html",
            {
                "experiences": experiences,
                "events": events,
                "talents": talents,
                "success": (
                    "Your booking has been submitted "
                    "successfully!"
                ),
            },
        )

    return render(
        request,
        "hub/booking.html",
        {
            "experiences": experiences,
            "events": events,
            "talents": talents,
        },
    )


def submit_event(request):

    if request.method == "POST":

        EventSubmission.objects.create(
            name=request.POST.get(
                "name",
                ""
            ).strip(),

            description=request.POST.get(
                "description",
                ""
            ).strip(),

            location=request.POST.get(
                "location",
                ""
            ).strip(),

            date=request.POST.get(
                "date"
            ),

            price=request.POST.get(
                "price"
            ) or 0,

            organizer_name=request.POST.get(
                "organizer_name",
                ""
            ).strip(),

            organizer_email=request.POST.get(
                "organizer_email",
                ""
            ).strip(),

            image=request.FILES.get(
                "image"
            ),
        )

        return render(
            request,
            "hub/submit_event.html",
            {
                "success": (
                    "Thank you! Your event has been "
                    "submitted and is waiting for approval."
                )
            },
        )

    return render(
        request,
        "hub/submit_event.html"
    )


def submit_experience(request):

    if request.method == "POST":

        ExperienceSubmission.objects.create(
            name=request.POST.get(
                "name",
                ""
            ).strip(),

            description=request.POST.get(
                "description",
                ""
            ).strip(),

            location=request.POST.get(
                "location",
                ""
            ).strip(),

            price=request.POST.get(
                "price"
            ) or 0,

            organizer_name=request.POST.get(
                "organizer_name",
                ""
            ).strip(),

            organizer_email=request.POST.get(
                "organizer_email",
                ""
            ).strip(),

            image=request.FILES.get(
                "image"
            ),
        )

        return render(
            request,
            "hub/submit_experience.html",
            {
                "success": (
                    "Thank you! Your experience has "
                    "been submitted and is waiting "
                    "for approval."
                )
            },
        )

    return render(
        request,
        "hub/submit_experience.html"
    )

