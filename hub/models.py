from django.db import models


class Experience(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

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
    price = models.DecimalField(max_digits=10, decimal_places=2)

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
    price = models.DecimalField(max_digits=10, decimal_places=2)

    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    experience = models.ForeignKey(
        Experience,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    travel = models.ForeignKey(
        Travel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name