from django.urls import path
from .views import ruyxat, create

urlpatterns = [
    path('', ruyxat, name='ruyxat'),
    path('create', create, name='create'),
]