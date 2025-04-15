from django.shortcuts import render


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

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')