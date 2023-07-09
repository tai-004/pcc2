from django import forms
from .models import Voluntario, Curriculo
from django.forms.widgets import FileInput
from django.contrib.auth.forms import User

class voluntarioForm(forms.Form):
    voluntario = forms.CharField(label='Digite o nome da vaga procurada.')
    
class NewVoluntarioForm(forms.ModelForm):
     class Meta:
        model = Voluntario
        fields =  ('titulo', 'horario', 'funcao', 'quantidadepessoas', 'tempo', 'idademinima', 'cidade', 'rua', 'bairro', 'numero', 'telefone')


class pesquisaForm(forms.Form):
    pesquisa = forms.CharField()

class NovoCurriculoForm(forms.ModelForm):
     class Meta:
        model = Curriculo
        fields = ('data_nasc', 'telefone', 'email', 'tempo_disponivel', 'motivacao', 'resumo')

