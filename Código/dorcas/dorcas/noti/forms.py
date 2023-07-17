from django import forms
from .models import Tabela_notis
from django.forms.widgets import FileInput
from django.contrib.auth.forms import User


#a instituição avalia o voluntario
class Tabela_notisForm(forms.ModelForm):
     class Meta:
        model = Tabela_notis
        fields =  ('cargo', 'desempenho', 'nota')

class LidoForm(forms.ModelForm):
     class Meta:
        model = Tabela_notis
        fields =  ('lido', )
