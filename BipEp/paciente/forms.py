from django import forms
from .models import Consultas

class ConsultaForm(forms.ModelForm):  
    class Meta:  
        model = Consultas  
        fields = "__all__"  