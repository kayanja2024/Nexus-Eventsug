from django.core.validators import RegexValidator
from django.db import models

PHONE_VALIDATOR = RegexValidator(
    regex=r'^[0-9+\-() ]{7,20}$',
    message="Enter a valid phone number, for example +256 701 234 567.",
)


class Booking(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("in_review", "In Review"),
        ("confirmed", "Confirmed"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, validators=[PHONE_VALIDATOR])
    event_type = models.CharField(max_length=100)
    event_date = models.DateField()
    location = models.CharField(max_length=150)
    budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.event_type}"
