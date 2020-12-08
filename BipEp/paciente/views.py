from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Usuario
from .models import Consultas
from .models import Exames
from datetime import datetime
from django.utils import formats
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    dados =  Usuario.objects.all()
    print(dados)
    args = {'usuario': dados}
    return render(request, 'htmlPaciente/home.html', args)

@login_required
def chat(request):
    return render(request, 'htmlPaciente/chatHome.html')

@login_required
def consultas(request):
    consultas = Consultas.objects.filter(idusuario = request.user)
    return render(request, 'htmlPaciente/consultas.html', {'consultas': consultas})

@login_required
def exames(request):
    exames = Exames.objects.filter(idusuario = request.user)
    return render(request, 'htmlPaciente/exames.html', {'exames': exames})
