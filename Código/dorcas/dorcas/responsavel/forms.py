

from .models import Responsavel
from django.forms.widgets import FileInput
from django.forms.models import ModelForm



from .models import Responsavel
from django import forms


class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = Responsavel
        fields = ["nome", "idade", "parentesco", "cpf", "cidade", "rua", "numero", "bairro", "telefone"]


        