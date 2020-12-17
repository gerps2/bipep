from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('acessonegado/', views.acessonegado),
    path('cadastrar/', views.cadastrarUsuario),
    path('etnia/', views.etniaSalvar),
]