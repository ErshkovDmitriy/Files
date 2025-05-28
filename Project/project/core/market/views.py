from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db import transaction

from .forms import CustomUserRegistrationForm, CustomerProfileForm, UserForm
from .models import CustomerProfile, ExpertProfile, Task

User = get_user_model()

# Основные страницы
def index(request):
    return render(request, 'base.html')

def about_project(request):
    return render(request, 'about_project.html')

def services(request):
    return render(request, 'services.html')

def partners(request):
    return render(request, 'partners.html')

def contacts(request):
    return render(request, 'contacts.html')

# Тестовая отправка письма
def test_email(request):
    send_mail(
        'Тестовое письмо',
        'Это письмо отправлено через Mailtrap.',
        settings.DEFAULT_FROM_EMAIL,
        ['your@mail.com'],
    )
    return HttpResponse("Письмо отправлено!")

# Регистрация и активация аккаунта
def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            if user.role == 'customer':
                CustomerProfile.objects.create(user=user)
            elif user.role == 'expert':
                ExpertProfile.objects.create(user=user)

            subject = 'Подтверждение регистрации'
            context = {
                'user': user,
                'domain': settings.DOMAIN,
                'protocol': settings.PROTOCOL,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            }

            text_message = render_to_string('registration/activation_email.txt', context)
            html_message = render_to_string('registration/activation_email.html', context)

            email = EmailMultiAlternatives(
                subject, text_message, settings.DEFAULT_FROM_EMAIL, [user.email]
            )
            email.attach_alternative(html_message, "text/html")
            email.send()

            return render(request, 'registration/email_sent.html')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return render(request, 'registration/activation_failed.html')

# Единый личный кабинет
@login_required
def personal_account_view(request):
    user = request.user

    if user.role == 'customer':
        profile = get_object_or_404(CustomerProfile, user=user)

        if request.method == 'POST':
            user_form = UserForm(request.POST, request.FILES, instance=user)
            profile_form = CustomerProfileForm(request.POST, instance=profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()

                return redirect('personal_account')
        else:
            user_form = UserForm(instance=user)
            profile_form = CustomerProfileForm(instance=profile)

        orders = Task.objects.filter(customer=user).order_by('-created_at')

        return render(request, 'customer_personal_account.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'orders': orders,
        })

    elif user.role == 'expert':
        profile = get_object_or_404(ExpertProfile, user=user)
        return render(request, 'expert_personal_account.html', {
            'user': user,
            'profile': profile,
        })

    else:
        return redirect('login')

# Удалён старый customer_dashboard

@login_required
def expert_dashboard(request):
    if request.user.role != 'expert':
        return redirect('personal_account')

    profile = get_object_or_404(ExpertProfile, user=request.user)

    return render(request, 'expert_dashboard.html', {
        'profile': profile,
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('personal_account')
        else:
            messages.error(request, 'Неправильный логин или пароль')
    return render(request, 'login.html')
