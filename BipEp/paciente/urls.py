from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('chat/', views.chat, name='chat'),
    path('consultas/', views.consultas, name='consultas'),
    path('exames/', views.exames, name='exames'),
    path('exames/', views.exames, name='exames'),
    path('datas/', views.datas, name='hello'),
    path('horarios/<str:data>', views.horario, name='horario'),
    path('salvarconsultas/', views.salvarConsultas, name='salvarconsultas'),
    path('salvarexames/', views.salvarExames, name='salvarexames'),
    path('examesconsulta/', views.examesConsultas, name='salvarexames'),
]