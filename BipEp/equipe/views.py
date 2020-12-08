from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'htmlEquipe/home.html')

def cadastro(request):
    return render(request, 'htmlEquipe/cadastro.html')