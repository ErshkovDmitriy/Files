from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('list_tasks', views.list_tasks, name='list_tasks'),
   path('add', views.add, name='add'),
   path('<int:pk>', views.EditDetailView.as_view(), name='edit'),
   path('<int:pk>/update', views.TaskUpdateView.as_view(), name='edit'),
]
