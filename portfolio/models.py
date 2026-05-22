from django.db import models


class GalleryItem(models.Model):
    CATEGORY_CHOICES = [
        ("wedding", "Wedding"),
        ("corporate", "Corporate"),
        ("concert", "Concert"),
        ("party", "Party"),
        ("other", "Other"),
    ]
    MEDIA_TYPE_CHOICES = [("image", "Image"), ("video", "Video")]

    title = models.CharField(max_length=150)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="other")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default="image")
    media_file = models.FileField(upload_to="portfolio/", blank=True, null=True)
    external_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    event_date = models.DateField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
