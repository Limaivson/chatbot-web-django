from django.urls import path
from . import views

urlpatterns = [
    path('texto/', views.texto, name='texto'),
]