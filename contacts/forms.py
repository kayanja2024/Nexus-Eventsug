from django import forms
from django.core.validators import RegexValidator

from .models import ContactMessage

PHONE_VALIDATOR = RegexValidator(
    regex=r'^[0-9+\-() ]{7,20}$',
    message="Enter a valid phone number, for example +256 701 234 567.",
)


class ContactForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "you@example.com",
                "autocomplete": "email",
            }
        ),
    )
    phone = forms.CharField(
        required=False,
        validators=[PHONE_VALIDATOR],
        widget=forms.TextInput(
            attrs={
                "placeholder": "+256 701 234 567",
                "inputmode": "tel",
            }
        ),
    )

    class Meta:
        model = ContactMessage
        fields = ["full_name", "email", "phone", "subject", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
            "full_name": forms.TextInput(attrs={"placeholder": "Full name"}),
            "subject": forms.TextInput(attrs={"placeholder": "Subject"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            classes = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (classes + " form-input").strip()
            field.widget.attrs.setdefault("autocomplete", "off")
