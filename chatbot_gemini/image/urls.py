from django.urls import path
from . import views

urlpatterns = [
    path('imagem/', views.image, name='texto'),
    path('send-image', views.send_image, name='message'),
]
