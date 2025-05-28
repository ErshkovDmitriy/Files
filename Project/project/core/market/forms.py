from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import CustomerProfile, ExpertProfile, UserRole, Task

User = get_user_model()


class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    role = forms.ChoiceField(choices=UserRole.choices, label="Кто вы?")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')
        labels = {
            'username': 'Логин',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'avatar': 'Аватар',
        }

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            valid_extensions = ['.jpg', '.jpeg', '.png']
            if not any(str(avatar.name).lower().endswith(ext) for ext in valid_extensions):
                raise ValidationError("Допустимые форматы изображений: .jpg, .jpeg, .png")
        return avatar


class CustomerProfileForm(forms.ModelForm):
    phone = PhoneNumberField(label='Номер телефона', required=False, region='RU')

    class Meta:
        model = CustomerProfile
        fields = ['phone', 'birth_date', 'city', 'education', 'faculty', 'specialty']
        labels = {
            'birth_date': 'Дата рождения',
            'city': 'Город',
            'education': 'Учебное заведение',
            'faculty': 'Факультет',
            'specialty': 'Специальность',
        }
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ExpertProfileForm(forms.ModelForm):
    class Meta:
        model = ExpertProfile
        fields = ['university', 'specialty', 'graduation_year', 'city', 'diploma_image', 'social_link']
        labels = {
            'university': 'Учебное заведение',
            'specialty': 'Специальность',
            'graduation_year': 'Год окончания',
            'city': 'Город проживания',
            'diploma_image': 'Фото диплома с вкладышем',
            'social_link': 'Ссылка на соцсети',
        }
        widgets = {
            'graduation_year': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
        }

    def clean_diploma_image(self):
        image = self.cleaned_data.get('diploma_image')
        if image:
            valid_extensions = ['.jpg', '.jpeg', '.png']
            if not any(str(image.name).lower().endswith(ext) for ext in valid_extensions):
                raise ValidationError("Допустимые форматы диплома: .jpg, .jpeg, .png")
        return image


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['work_type', 'subject', 'title', 'description', 'deadline', 'attached_file']
        labels = {
            'work_type': 'Тип работы',
            'subject': 'Предмет',
            'title': 'Заголовок',
            'description': 'Описание задания',
            'deadline': 'Срок выполнения',
            'attached_file': 'Файл (необязательно)',
        }
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')
        if deadline and deadline < timezone.now().date():
            raise ValidationError("Срок выполнения не может быть в прошлом.")
        return deadline

    def clean_attached_file(self):
        file = self.cleaned_data.get('attached_file')
        if file:
            valid_extensions = ['.pdf', '.doc', '.docx', '.txt', '.zip', '.rar']
            if not any(str(file.name).lower().endswith(ext) for ext in valid_extensions):
                raise ValidationError("Недопустимый формат файла. Разрешены: .pdf, .doc, .docx, .txt, .zip, .rar")
        return file
