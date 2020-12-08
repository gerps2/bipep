from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils import formats
from django.contrib.auth.decorators import login_required
from datetime import datetime
from BipEp.models import Usuario
from BipEp.models import Consultas
from BipEp.models import Exames



@login_required
def home(request):
    dados = Usuario.objects.filter(id = 2)
    print(dados)
    args = {'usuario': dados}
    return render(request, 'htmlPaciente/home.html', args)

@login_required
def chat(request):
    return render(request, 'htmlPaciente/chatHome.html')

@login_required
def consultas(request):
    consultas = Consultas.objects.filter(idusuario = 2)
    return render(request, 'htmlPaciente/consultas.html', {'consultas': consultas})

@login_required
def exames(request):
    exames = Exames.objects.filter(idusuario = 2)
    return render(request, 'htmlPaciente/exames.html', {'exames': exames})
