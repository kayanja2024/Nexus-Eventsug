from django.urls import path

from .views import booking_create

urlpatterns = [
    path("", booking_create, name="booking_create"),
]
