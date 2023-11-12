from core.views import index, delete_everyone
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('delete', delete_everyone, name='delete_everyone'),
]
