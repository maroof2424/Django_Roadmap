from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", "email", "address"]
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class":"form-control"}),
            "address": forms.Textarea(attrs={"class":"form-control", "rows":3}),
        }
