from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "email", "rating", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Your Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Your Email"}),
            "rating": forms.NumberInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Your feedback"}),
        }
