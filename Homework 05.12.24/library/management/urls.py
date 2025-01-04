from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='base'),
     path('list_books', views.list_books, name='list_books'),
     path('list_users', views.list_users, name='list_users'),
     path('genres', views.genres, name='genres'),
     # path('books_by_genre', views.books_by_genre, name='books_by_genre'),
     path('books_by_genre/<int:genre_id>', views.books_by_genre, name='books_by_genre'),
     path('rent', views.rent, name='rent'),
]

