from django.contrib import admin

from .models import (
    Experience,
    Event,
    Talent,
    Booking,
    EventSubmission,
    ExperienceSubmission,
    CollectionItem,
)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "price",
        "available",
    )

    list_filter = (
        "available",
    )

    search_fields = (
        "name",
        "description",
        "location",
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "date",
        "price",
        "available",
    )

    list_filter = (
        "available",
        "date",
    )

    search_fields = (
        "name",
        "description",
        "location",
    )


@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "talent_type",
        "location",
        "price",
        "available",
    )

    list_filter = (
        "talent_type",
        "available",
    )

    search_fields = (
        "name",
        "description",
        "location",
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "talent",
        "experience",
        "event",
        "created_at",
    )

    list_filter = (
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
    )


@admin.register(EventSubmission)
class EventSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "date",
        "organizer_name",
        "organizer_email",
        "approved",
        "created_at",
    )

    list_filter = (
        "approved",
        "date",
    )

    search_fields = (
        "name",
        "location",
        "organizer_name",
        "organizer_email",
    )


@admin.register(ExperienceSubmission)
class ExperienceSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "organizer_name",
        "organizer_email",
        "approved",
        "created_at",
    )

    list_filter = (
        "approved",
        "created_at",
    )

    search_fields = (
        "name",
        "location",
        "organizer_name",
        "organizer_email",
    )


@admin.register(CollectionItem)
class CollectionItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "colour",
        "size",
        "price",
        "available",
    )

    list_filter = (
        "category",
        "colour",
        "size",
        "available",
    )

    search_fields = (
        "name",
        "description",
    )