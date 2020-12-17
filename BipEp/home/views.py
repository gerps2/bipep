from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils import formats
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from BipEp.models import Usuario
from BipEp.models import Etnia
from BipEp.models import Permissoes
from BipEp.models import Areasequipe
from BipEp.models import Hospitais
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
import datetime

@login_required
def home(request):
    usuario = Usuario.objects.filter(iduser = request.user).values('idpermissao')
    nome = Usuario.objects.filter(iduser = request.user).values('nome')
    print(usuario.get()['idpermissao'] == 2)
    if usuario.get()['idpermissao'] == 2:
        print('admin')
        return render(request, 'htmlHome/home.html',{'permissao': 2, 'nome': nome.get()['nome']})
    elif usuario.get()['idpermissao'] == 3:
        print('paciente')
        return render(request, 'htmlHome/home.html',{'permissao': 3, 'nome': nome.get()['nome']})
    elif usuario.get()['idpermissao'] == 4:
        print('equipe')
        return render(request, 'htmlHome/home.html',{'permissao': 4, 'nome': nome.get()['nome']})
    else:
        return render(request, 'htmlHome/acessoNegado.html') 
    
@login_required
def acessonegado(request):
    return render(request, 'htmlHome/acessoNegado.html')

@login_required
def cadastrarUsuario(request):
    usuario = Usuario.objects.filter(iduser = request.user).values('idpermissao')
    areas = Areasequipe.objects.all()
    hospital = Hospitais.objects.all()
    if request.method == 'POST':
        login = request.POST['login']
        senha = request.POST['Senha']
        nome = request.POST['nome']
        email = request.POST['email']
        dadosPermissao = int(request.POST['permissao'])
        permissao = Permissoes.objects.get(idpermissao = request.POST['permissao'])
        hospital = Hospitais.objects.get(idhospital = 2)
        if dadosPermissao == 2:
            print(request.POST)
            print('admin')
            usuariosalvo = User.objects.create_user(password = senha, username = login)
            print('salvei usuario')
            dados = Usuario(nome = nome, email= email, idpermissao=permissao, idhospital = hospital,iduser=usuariosalvo, isequipe=True, areaequipe=0)
            dados.save()
            print('preenchi os dados do usuario')
            print(dados)
            return render(request, 'htmlHome/cadastrarUsuario.html', {'cadastrado': True})
        if dadosPermissao == 3:
            print(request.POST)
            print('paciente')
            usuariosalvo = User.objects.create_user(password = senha, username = login)
            print('salvei usuario')
            dados = Usuario(nome = nome, email= email, idpermissao=permissao, idhospital = hospital,iduser=usuariosalvo, isequipe=True, areaequipe=0)
            dados.save()
            print('preenchi os dados do usuario')
            print(dados)
            return render(request, 'htmlHome/cadastrarUsuario.html', {'cadastrado': True})
        if dadosPermissao == 4:
            print(request.POST)
            print('equipe')
            usuariosalvo = User.objects.create_user(password = senha, username = login)
            print('salvei usuario')
            dados = Usuario(nome = nome, email= email, idpermissao=permissao, idhospital = hospital,iduser=usuariosalvo, isequipe=True, areaequipe=0)
            dados.save()
            print('preenchi os dados do usuario')
            print(dados)
            return render(request, 'htmlHome/cadastrarUsuario.html', {'cadastrado': True})
    elif usuario.get()['idpermissao'] == 2:
        return render(request, 'htmlHome/cadastrarUsuario.html', {'hospitais': hospital, 'areas': areas, 'cadastrado': False})
    else:
        return render(request, 'htmlHome/acessoNegado.html')
    
@api_view(['POST'])
def etniaSalvar(request):
    if request.data != None:
        dados = Etnia(nome = request.data['nome'])
        dados.save()
        return Response({'sucesso': True})
    else:
        return Response({'sucesso': False}) 