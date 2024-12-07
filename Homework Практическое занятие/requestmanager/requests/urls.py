from django.urls import path
from . import views

urlpatterns = [
    path("", views.create_request, name="create"),
    path("request_list", views.request_list, name="request_list"),
]
