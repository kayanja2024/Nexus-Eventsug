from django import forms
from django.core.validators import RegexValidator

from .models import Booking

PHONE_VALIDATOR = RegexValidator(
    regex=r'^\d{7,20}$',
    message="Enter a valid phone number using digits only.",
)


class BookingForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "you@example.com",
                "autocomplete": "email",
            }
        ),
    )
    phone = forms.CharField(
        required=True,
        validators=[PHONE_VALIDATOR],
        widget=forms.TextInput(
            attrs={
                "type": "tel",
                "placeholder": "0701234567",
                "autocomplete": "tel",
                "inputmode": "numeric",
                "pattern": "[0-9]*",
                "title": "Numbers only",
                "oninput": "this.value=this.value.replace(/[^0-9]/g, '')",
            }
        ),
    )

    class Meta:
        model = Booking
        fields = [
            "full_name",
            "email",
            "phone",
            "event_type",
            "event_date",
            "location",
            "budget",
            "message",
        ]
        widgets = {
            "event_date": forms.DateInput(attrs={"type": "date"}),
            "message": forms.Textarea(attrs={"rows": 4}),
            "full_name": forms.TextInput(attrs={"placeholder": "Full name"}),
            "event_type": forms.TextInput(attrs={"placeholder": "Event type"}),
            "location": forms.TextInput(attrs={"placeholder": "Location"}),
            "budget": forms.NumberInput(attrs={"placeholder": "Budget"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.required = True
            classes = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (classes + " form-input").strip()
            field.widget.attrs.setdefault("autocomplete", "off")
