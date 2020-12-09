from django import forms
from BipEp.models import Consultas
from django import forms


class ConsultaForm(forms.ModelForm):  
    class Meta:
        model = Consultas
        fields = ("__all__")