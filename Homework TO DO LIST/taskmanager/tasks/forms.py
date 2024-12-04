from .models import Task
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, CheckboxInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed', 'created_at']

        widgets = {
            "title": TextInput(attrs={
                'placeholder': 'Название задачи'
            }),
            "description": Textarea(attrs={
                'placeholder': 'Описание задачи'
            }),
            "is_completed": CheckboxInput(attrs={
                'placeholder': 'Статус задачи'
            }),
            "created_at": DateTimeInput(),
        }
