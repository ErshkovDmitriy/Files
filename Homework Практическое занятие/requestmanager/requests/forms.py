from .models import Request
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, EmailInput


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'email', 'message', 'submitted_at']

        widgets = {
            "name": TextInput(attrs={
                'placeholder': 'Имя'
            }),
            "email": EmailInput(attrs={
                'placeholder': 'email'
            }),
            "message": Textarea(attrs={
                'placeholder': 'Текстовое поле'
            }),
            "submitted_at": DateTimeInput(),
        }
