from django.urls import path
from . import views

urlpatterns = [
    path('image/', views.image, name='image'),
    path('send-image/', views.send_image, name='send-image'),
    path('text/', views.texto, name='texto'),
    path('send-text', views.message, name='send-text'),
    path('', views.index, name='index'),
]
