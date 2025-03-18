from django.contrib import admin
from .models import Book, User, Rental, Genre

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Rental)
admin.site.register(Genre)

admin.site.site_header = "Управление проектами"
admin.site.site_title = "Админка Library Manager"
admin.site.index_title = "Добро пожаловать в Library Manager"
