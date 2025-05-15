from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from .forms import CustomUserRegistrationForm  # форма регистрации
from .models import CustomerProfile, ExpertProfile


User = get_user_model()

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

def login(request):
    return render(request, 'login.html')

def test_email(request):
    send_mail(
        'Тестовое письмо',
        'Это письмо отправлено через Mailtrap.',
        'noreply@example.com',  # <-- from_email
        ['your@mail.com'],
    )
    return HttpResponse("Письмо отправлено!")

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False

            # Получаем и валидируем роль
            role = request.POST.get('role')
            if role not in ['customer', 'expert']:
                form.add_error(None, "Некорректная роль.")
                return render(request, 'registration/register.html', {'form': form})
            user.role = role
            user.save()

            if user.role == 'customer':
                CustomerProfile.objects.create(user=user)
            elif user.role == 'expert':
                ExpertProfile.objects.create(user=user)

            # Отправка письма для активации
            current_site = get_current_site(request)
            subject = 'Подтверждение регистрации'
            message = render_to_string('registration/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            send_mail(subject, message, 'noreply@yourdomain.com', [user.email])

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
        return redirect('login')  # Можно заменить на redirect в личный кабинет
    else:
        return render(request, 'registration/activation_failed.html')
