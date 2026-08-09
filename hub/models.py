from django.db import models


class Experience(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to="experiences/",
        blank=True,
        null=True
    )

    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to="events/",
        blank=True,
        null=True
    )

    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Travel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    destination = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Talent(models.Model):
    TALENT_TYPES = [
        ("MC", "MC"),
        ("DJ", "DJ"),
        ("HYPEMAN", "Hypeman"),
        ("DANCER", "Dancer"),
    ]

    name = models.CharField(max_length=200)

    talent_type = models.CharField(
        max_length=20,
        choices=TALENT_TYPES
    )

    description = models.TextField()

    location = models.CharField(max_length=200)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to="talent/",
        blank=True,
        null=True
    )

    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.get_talent_type_display()}"


class Booking(models.Model):
    name = models.CharField(max_length=200)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    talent = models.ForeignKey(
        Talent,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    talent_custom = models.CharField(
        max_length=200,
        blank=True,
        default=""
    )

    experience = models.ForeignKey(
        Experience,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    experience_custom = models.CharField(
        max_length=200,
        blank=True,
        default=""
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    event_custom = models.CharField(
        max_length=200,
        blank=True,
        default=""
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class EventSubmission(models.Model):
    name = models.CharField(max_length=200)

    description = models.TextField()

    location = models.CharField(max_length=200)

    date = models.DateField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    organizer_name = models.CharField(
        max_length=200
    )

    organizer_email = models.EmailField()

    image = models.ImageField(
        upload_to="event_submissions/",
        blank=True,
        null=True
    )

    approved = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class ExperienceSubmission(models.Model):
    name = models.CharField(max_length=200)

    description = models.TextField()

    location = models.CharField(max_length=200)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    organizer_name = models.CharField(
        max_length=200
    )

    organizer_email = models.EmailField()

    image = models.ImageField(
        upload_to="experience_submissions/",
        blank=True,
        null=True
    )

    approved = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


# =========================================
# EXPERIENCE HUB COLLECTION
# =========================================

class CollectionItem(models.Model):

    CATEGORY_CHOICES = [
        ("HOODIE", "Hoodie"),
        ("TSHIRT", "T-Shirt"),
    ]

    COLOUR_CHOICES = [
        ("Black", "Black"),
        ("White", "White"),
        ("Red", "Red"),
        ("Yellow", "Yellow"),
        ("Pink", "Pink"),
    ]

    SIZE_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "Extra Large"),
        ("XXL", "2XL"),
    ]

    name = models.CharField(max_length=200)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    colour = models.CharField(
        max_length=20,
        choices=COLOUR_CHOICES
    )

    size = models.CharField(
        max_length=10,
        choices=SIZE_CHOICES
    )

    image = models.ImageField(
        upload_to="collection/",
        blank=True,
        null=True
    )

    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} ({self.colour} - {self.size})"