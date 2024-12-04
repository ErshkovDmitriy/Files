from django.shortcuts import render, redirect
from .models import Request
from .forms import RequestForm


def request_list(request):
    applications = Request.objects.all()
    return render(request, 'requests/request_list.html', {'applications': applications})


def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_list')

    form = RequestForm()
    date = {
        'form': form,
    }
    return render(request, 'requests/create.html', date)

