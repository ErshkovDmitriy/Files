from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="base"),
    path("about_project/", views.about_project, name="about_project"),
    path("services/", views.services, name="services"),
    path("partners/", views.partners, name="partners"),
    path("contacts/", views.contacts, name="contacts"),

]
