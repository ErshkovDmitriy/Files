from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="base"),
    path("about_project/", views.about_project, name="about_project"),
    path("services/", views.services, name="services"),
    path("partners/", views.partners, name="partners"),
    path("contacts/", views.contacts, name="contacts"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('test-email/', views.test_email),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('dashboard/', views.personal_account_view, name='personal_account'),

    # Если пока нужен expert_dashboard отдельно — оставлю
    path('dashboard/expert/', views.expert_dashboard, name='expert_dashboard'),
]
