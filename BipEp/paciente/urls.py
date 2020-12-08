from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('chat/', views.chat, name='chat'),
    path('consultas/', views.consultas, name='consultas'),
    path('exames/', views.exames, name='exames'),
]