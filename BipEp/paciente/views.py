from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils import formats
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.decorators import permission_required
from BipEp.models import Usuario
from BipEp.models import Consultas
from BipEp.models import Exames
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
from .forms import ConsultaForm



@login_required
def home(request):
    dados = Usuario.objects.filter(iduser = request.user)
    print(dados)
    args = {'usuario': dados, 'last_login': request.user.last_login}
    return render(request, 'htmlPaciente/home.html', args)


@login_required
def chat(request):
    return render(request, 'htmlPaciente/chatHome.html')

@login_required
def consultas(request):
    consultas = Consultas.objects.filter(idusuario = request.user.id)
    return render(request, 'htmlPaciente/consultas.html', {'consultas': consultas})

@login_required
def exames(request):
    print(request.user)
    exames = Exames.objects.filter(idusuario = request.user.id)
    return render(request, 'htmlPaciente/exames.html', {'exames': exames})


@login_required
def alterarConsulta(request, idconsulta):
    dados = get_object_or_404(Consultas, pk=idconsulta)
    form = ConsultaForm(instance=dados)
    
    if(request.method == 'POST'):
        return False
    else:
        return render(request, 'consultas/editarConsulta.html', {'form': form, 'dados': dados})
