from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title","description","complete"]
        widgets = {
            'title': forms.TextInput(attrs={
                "class":"form-control",
                "placeholder" : "Enter task title",
            }),
            "description": forms.Textarea(attrs={
                "class":"form-control",
                "rows":3,
                "placeholder": "Enter task details",
            }),
            "complete":forms.CheckboxInput(attrs={
                'class':'form-check-input',
            })
        }