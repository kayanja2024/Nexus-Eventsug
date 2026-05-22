from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            message_obj = form.save()
            send_mail(
                subject=f"New contact message: {message_obj.subject}",
                message=(
                    f"From: {message_obj.full_name}\n"
                    f"Email: {message_obj.email}\n"
                    f"Phone: {message_obj.phone}\n\n"
                    f"{message_obj.message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.BOOKINGS_NOTIFICATION_EMAIL],
                fail_silently=True,
            )
            messages.success(request, "Message sent successfully. We will contact you soon.")
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "contacts/form.html", {"form": form})
