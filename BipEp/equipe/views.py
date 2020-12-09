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
from BipEp.models import Estatistica



@login_required
def home(request):
    dados = Usuario.objects.filter(id = 2)
    args = {'usuario': dados}
    return render(request, 'htmlEquipe/home.html', args)



@login_required
def cadastro(request):
    return render(request, 'htmlEquipe/cadastro.html')



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

