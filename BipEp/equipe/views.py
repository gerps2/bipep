from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils import formats
from django.contrib.auth.decorators import login_required
from datetime import datetime
from BipEp.models import Usuario
from BipEp.models import Consultas
from BipEp.models import Exames



def home(request):
    dados = Usuario.objects.filter(id = 2)
    args = {'usuario': dados}
    return render(request, 'htmlEquipe/home.html', args)

def cadastro(request):
    return render(request, 'htmlEquipe/cadastro.html')

def areamedica(request):
    return render(request, 'htmlEquipe/areamedica.html')

def areaenfermagem(request):
    return render(request, 'htmlEquipe/areaenfermagem.html')

def areaneuropsicologia(request):
    return render(request, 'htmlEquipe/areaneuropsicologia.html')

def areaeeg(request):
    return render(request, 'htmlEquipe/areaeeg.html')

def arearnm(request):
    return render(request, 'htmlEquipe/arearnm.html')

def areatc(request):
    return render(request, 'htmlEquipe/areatc.html')

def areaclinica(request):
    return render(request, 'htmlEquipe/areaclinica.html')

def areabiologiamolecular(request):
    return render(request, 'htmlEquipe/areabiologiamolecular.html')

def areapesquisacientifica(request):
    return render(request, 'htmlEquipe/areapesquisacientifica.html')

def qualidadevida(request):
    return render(request, 'htmlEquipe/qualidadevida.html')

