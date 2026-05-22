from django.shortcuts import render

from .models import GalleryItem


def gallery(request):
    items = GalleryItem.objects.all()
    return render(request, "portfolio/gallery.html", {"items": items})

# Create your views here.
