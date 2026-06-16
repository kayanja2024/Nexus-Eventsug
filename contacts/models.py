from django.core.validators import RegexValidator
from django.db import models

PHONE_VALIDATOR = RegexValidator(
    regex=r'^[0-9+\-() ]{7,20}$',
    message="Enter a valid phone number, for example +256 701 234 567.",
)


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(
        max_length=30,
        blank=True,
        validators=[PHONE_VALIDATOR],
    )
    subject = models.CharField(max_length=180)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.subject}"
