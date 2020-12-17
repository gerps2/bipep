from django.shortcuts import render
from django.http import HttpResponse
from django.utils import formats
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from BipEp.models import Usuario
from BipEp.models import Consultas
from BipEp.models import Exames
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
import datetime




@login_required
def home(request):
    usuario = Usuario.objects.filter(iduser = request.user).values('idpermissao')
    nome = Usuario.objects.filter(iduser = request.user).values('nome')
    lastlogin = User.objects.get(username = request.user).last_login
    print(usuario.get()['idpermissao'] == 2)
    if usuario.get()['idpermissao'] == 3:
        print('paciente')
        return render(request, 'htmlPaciente/home.html',{'permissao': 3, 'nome': nome.get()['nome'], 'lastlogin': lastlogin})
    elif usuario.get()['idpermissao'] == 2:
        print('admin')
        return render(request, 'htmlPaciente/home.html',{'permissao': 2, 'nome': nome.get()['nome'], 'lastlogin': lastlogin})
    else:
        return render(request, 'htmlHome/acessoNegado.html') 
    
    
@login_required
def chat(request):
    return render(request, 'htmlPaciente/chatHome.html')

@login_required
def consultas(request):
    usuarios = Usuario.objects.get(iduser = request.user.id)
    consultas = Consultas.objects.filter(idusuario = usuarios.id)
    print(consultas)
    return render(request, 'htmlPaciente/consultas.html', {'consultas': consultas})

@login_required
def exames(request):
    usuarios = Usuario.objects.get(iduser = request.user.id)
    exames = Exames.objects.filter(idusuario = usuarios.id)
    return render(request, 'htmlPaciente/exames.html', {'exames': exames})

@login_required
def alterarConsulta(request, id):
    return render(request, 'consultas/editarConsulta.html')

@login_required
def examesConsultas(request):
    return render(request, 'htmlPaciente/examesConsulta.html')

@api_view(['POST'])
def salvarConsultas(request):
    if request.data != None:
        consulta = Consultas.objects.get(idconsulta = request.data['id'])
        print('------------------------------------------------------------------')
        datas  = request.data['novaData'].replace('-', '/')
        novaData = datetime.datetime.strptime(datas, "%d/%m/%Y").strftime("%Y-%m-%d")
        consulta.data = novaData
        consulta.hora = request.data['horarioNovo']
        consulta.save()
        print('------------------------------------------------------------------')
        return Response({'sucesso': True}) 
    else:
        return Response({'sucesso': False}) 
    
@api_view(['POST'])
def salvarExames(request):
    if request.data != None:
        exame = Exames.objects.get(idexame = request.data['id'])
        print('------------------------------------------------------------------')
        datas  = request.data['novaData'].replace('-', '/')
        novaData = datetime.datetime.strptime(datas, "%d/%m/%Y").strftime("%Y-%m-%d")
        exame.data = novaData
        exame.hora = request.data['horarioNovo']
        exame.save()
        print('------------------------------------------------------------------')
        return Response({'sucesso': True}) 
    else:
        return Response({'sucesso': False}) 

@api_view(['GET'])
def datas(request):
    dados = [{"data":"18-12-2020"},{"data":"19-12-2020"}, {"data":"20-12-2020"}, {"data":"21-12-2020"},{"data":"22-12-2020"},{"data":"23-12-2020"}]
    return Response(dados)

@api_view(['GET'])
def horario(request, data):
    if data == "18-12-2020":
        dados = [{"hora": "09:00"}, {"hora": "09:30"}, {"hora": "10:00"},{"hora": "10:30"},{"hora": "11:00"},{"hora": "11:30"}]
        return Response(dados)
    elif data == "19-12-2020":
        dados = [{"hora": "12:00"}, {"hora": "12:30"}, {"hora": "13:00"},{"hora": "13:30"},{"hora": "14:00"},{"hora": "14:30"}]
        return Response(dados)
    elif data == "20-12-2020":
        dados = [{"hora": "15:00"}, {"hora": "15:30"}, {"hora": "16:00"},{"hora": "16:30"},{"hora": "17:00"},{"hora": "17:30"}]
        return Response(dados)
    elif data == "21-12-2020":
        dados = [{"hora": "18:00"}, {"hora": "18:30"}, {"hora": "19:00"},{"hora": "19:30"},{"hora": "20:00"},{"hora": "20:30"}]
        return Response(dados)
    elif data == "22-12-2020":
        dados = [{"hora": "21:00"}, {"hora": "21:30"}, {"hora": "22:00"},{"hora": "22:30"},{"hora": "23:00"},{"hora": "23:30"}]
        return Response(dados)
    elif data == "23-12-2020":
        dados = [{"hora": "09:00"}, {"hora": "09:30"}, {"hora": "10:00"},{"hora": "10:30"},{"hora": "11:00"},{"hora": "11:30"}]
        return Response(dados)
    else:
        return Response({'horarios': ""})
    
    
