from django import forms


from django import forms
from responsavel.models import Responsavel

class ResponsavelForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(), max_length=100, required=False)
    parentesco = forms.CharField(widget=forms.TextInput(), max_length=100, required=False)
    telefone = forms.CharField(widget=forms.TextInput(), max_length=20, required=False)
    idade = forms.DateInput(attrs={'required': False})
    cidade = forms.CharField(widget=forms.TextInput(), max_length=150, required=False)
    rua = forms.CharField(widget=forms.TextInput(), max_length=150, required=False)
    numero = forms.CharField(widget=forms.TextInput(), max_length=10, required=False)
    bairro = forms.CharField(widget=forms.TextInput(), max_length=150, required=False)
    cpf = forms.IntegerField(required=False)
  

    class Meta:
        model = Responsavel
        fields = ('nome', 'parentesco' ,'telefone', 'idade', 'cidade', 'rua', 'numero', 'bairro', 'cpf')

