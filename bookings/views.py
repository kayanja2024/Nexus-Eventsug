from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import BookingForm


def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            send_mail(
                subject="New booking request received",
                message=(
                    f"Booking from {booking.full_name}\n"
                    f"Event: {booking.event_type}\n"
                    f"Date: {booking.event_date}\n"
                    f"Phone: {booking.phone}\n"
                    f"Email: {booking.email}\n"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.BOOKINGS_NOTIFICATION_EMAIL],
                fail_silently=True,
            )
            messages.success(request, "Your booking request has been submitted successfully.")
            return redirect("booking_create")
    else:
        form = BookingForm()

    return render(request, "bookings/form.html", {"form": form})
