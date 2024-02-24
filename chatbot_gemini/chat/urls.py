from django.urls import path
from . import views

urlpatterns = [
    path('chat-bot/', views.texto, name='texto'),
    path('send', views.message, name='message'),
]
