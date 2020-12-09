from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def logar(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        print('nao foi dessa vez')