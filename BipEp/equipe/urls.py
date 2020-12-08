from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('cadastro', views.cadastro),
    path('areamedica/acompanhamento', views.areamedica),
    path('areaenfermagem/acompanhamento', views.areaenfermagem),
    path('areaneuropsicologia/acompanhamento', views.areaneuropsicologia),
    path('areaeeg/acompanhamento', views.areaeeg),
    path('arearnm/acompanhamento', views.arearnm),
    path('areatc/acompanhamento', views.areatc),
    path('areaclinica/acompanhamento', views.areaclinica),
    path('areabiologiamolecular/acompanhamento', views.areabiologiamolecular),
    path('areapesquisacientifica/acompanhamento', views.areapesquisacientifica),
    path('qualidadevida/acompanhamento', views.qualidadevida)
]