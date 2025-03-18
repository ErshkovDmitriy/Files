from django.shortcuts import render
from .models import Book, User, Rental, Genre
from .forms import RentalForm


def index(request):
    return render(request, 'base.html')


def rent(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data['user']
            book = form.cleaned_data['book']
            rental_date = form.cleaned_data['rental_date']
            return_date = form.cleaned_data['return_date']

            rental = form.save()

            book.is_available = False
            book.save()

            return render(request, 'management/list_books.html')

    else:
        form = RentalForm()

    return render(request, 'management/rent.html', {'form': form})


def list_books(request):
    books = Book.objects.filter(is_available=True)
    return render(request, 'management/list_books.html', {'books': books})


def list_users(request):
    users = User.objects.all()
    return render(request, 'management/list_users.html', {'users': users})


def genres(request):
    genres_list = Genre.objects.all()
    return render(request, 'management/genres.html', {'genres': genres_list})


def books_by_genre(request, genre_id):
    # genre = Genre.objects.get(pk=genre_id)
    books = Book.objects.filter(genre_id=genre_id)
    return render(request, 'management/books_by_genre.html', context={'books': books})


# def rent(request):
#     books = Book.objects.all()
#     return render(request, 'management/list_books.html', {'books': books})



