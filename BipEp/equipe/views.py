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
from BipEp.models import Paciente
from BipEp.models import Estatistica
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils import formats
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from BipEp.models import Usuario
from BipEp.models import Etnia
from BipEp.models import Consultas
from BipEp.models import Exames
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
import json
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
import datetime
from django.core import serializers




@login_required
def home(request):
    usuario = Usuario.objects.filter(iduser = request.user).values('idpermissao')
    nome = Usuario.objects.filter(iduser = request.user).values('nome')
    lastlogin = User.objects.get(username = request.user).last_login
    if usuario.get()['idpermissao'] == 4:
        print('paciente')
        return render(request, 'htmlEquipe/home.html',{'permissao': 3, 'nome': nome.get()['nome'], 'lastlogin': lastlogin})
    elif usuario.get()['idpermissao'] == 2:
        print('admin')
        return render(request, 'htmlEquipe/home.html',{'permissao': 2, 'nome': nome.get()['nome'], 'lastlogin': lastlogin})
    else:
        return render(request, 'htmlHome/acessoNegado.html') 
    

@login_required
def cadastro(request):
    return render(request, 'htmlEquipe/cadastro.html')

@login_required
def cadastroPaciente(request):
    return render(request, 'htmlEquipe/cadastropaciente.html')


@login_required
def areamedica(request):
    return render(request, 'htmlEquipe/areamedica.html')



@login_required
def areaenfermagem(request):
    return render(request, 'htmlEquipe/areaenfermagem.html')



@login_required
def areaneuropsicologia(request):
    return render(request, 'htmlEquipe/areaneuropsicologia.html')



@login_required
def areaeeg(request):
    return render(request, 'htmlEquipe/areaeeg.html')



@login_required
def arearnm(request):
    return render(request, 'htmlEquipe/arearnm.html')



@permission_required('polls.can_vote', login_url='/permissao')
@login_required
def areatc(request):
    return render(request, 'htmlEquipe/areatc.html')



@login_required
def areaclinica(request):
    return render(request, 'htmlEquipe/areaclinica.html')



@login_required
def areabiologiamolecular(request):
    return render(request, 'htmlEquipe/areabiologiamolecular.html')



@login_required
def areapesquisacientifica(request):
    return render(request, 'htmlEquipe/areapesquisacientifica.html')



@login_required
def qualidadevida(request):
    return render(request, 'htmlEquipe/qualidadevida.html')


@login_required
def graficos(request):
    return render(request, 'htmlEquipe/grafico.html')


@api_view(['GET'])
def getUsuarios(request):
    dados = serializers.serialize('json', Usuario.objects.all())
    return HttpResponse(dados,content_type="text/json-comment-filtered")

@api_view(['GET'])
def getEtnias(request):
    dados = serializers.serialize('json', Etnia.objects.all())
    return HttpResponse(dados,content_type="text/json-comment-filtered")

@api_view(['POST'])
def cadastrarPaciente(request):
    if request.data != None:
        getpaciente = Paciente.objects.get(idusuario = int(request.data['idusuario']))
        if getpaciente == None:
            getusuario = Usuario.objects.get(id = int(request.data['idusuario']))
            getetnia= Etnia.objects.get(idetnia = int(request.data['idetnia']))
            dataconvertida = request.data['dtnascimento'].replace('-', '/')
            dataNascimento = datetime.datetime.strptime(dataconvertida, "%d/%m/%Y").strftime("%Y-%m-%d")
            novaPaciente = Paciente(idusuario = getusuario.id, dtnascimento=dataNascimento, idetnia = getetnia, endereco=request.data['endereco'], telefone=request.data['telefone'], sexo=request.data['sexo'])
            novaPaciente.save()
            resposta = HttpResponse(json.dumps({'sucesso': True, 'message': 'Sucesso ao cadastrar paciente'}),content_type='application/json')
            resposta.status_code = 200
            return resposta
        else:
            resposta = HttpResponse(json.dumps({'sucesso': False, 'message': 'paciente ja cadastrado'}),content_type='application/json')
            resposta.status_code = 400
            return resposta
    else:
        resposta = HttpResponse(json.dumps({'sucesso': False, 'message': 'Sem informacoes no corpo do request'}),content_type='application/json')
        resposta.status_code = 400
        return resposta

