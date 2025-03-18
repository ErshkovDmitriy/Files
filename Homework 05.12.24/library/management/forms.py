from django.forms import ModelForm, Select, DateTimeInput
from .models import Rental, Book


class RentalForm(ModelForm):
    class Meta:
        model = Rental
        fields = ['user', 'book', 'rental_date', 'return_date']

        widgets = {
            'user': Select(attrs={
                'placeholder': 'пользователь'
            }),
            'book': Select(attrs={
                'placeholder': 'Книга'
            }),
            'rental_date': DateTimeInput(attrs={
                'placeholder': 'дата аренды'
            }),
            'return_date': DateTimeInput(attrs={
                'placeholder': 'дата возврата'
            })
        }
