from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from accounts.models import Profile



class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError("O email {} já está em uso.".format(e))

        return e




#class de formulario referente ao perfil do user comum
class EditProfileForm(forms.ModelForm):
            nome = forms.CharField(widget=forms.TextInput(), max_length=100, required=False)
            telefone = forms.CharField(widget=forms.TextInput(), max_length=20, required=False)
            formacao = forms.CharField(widget=forms.TextInput(), max_length=100, required=False)
            sexo = forms.CharField(widget=forms.TextInput(), required=False)
            idade = forms.DateTimeField(widget=forms.DateTimeField())
            trabalho = forms.CharField(widget=forms.TextInput(), max_length=150, required=False)
            habilidades = forms.CharField(widget=forms.TextInput(), max_length=150, required=False)
            cidade = forms.CharField(widget=forms.TextInput(), max_length=150, required=False)
            estado = forms.CharField(widget=forms.TextInput(), max_length=150, required=False)
            rua = forms.CharField(widget=forms.TextInput(), max_length=150, required=False)
            numero = forms.CharField(widget=forms.TextInput(), max_length=10, required=False)
            bairro = forms.CharField(widget=forms.TextInput(), max_length=150, required=False)
            cpf = forms.IntegerField(required=False)
            picture = forms.ImageField(required=False)
            banner = forms.ImageField(required=False)

            class Meta:
                model = Profile
                fields = ('nome', 'telefone', 'formacao','sexo', 'idade', 'trabalho', 'habilidades', 'cidade', 'estado', 'rua', 'numero', 'bairro', 'cpf', 'picture', 'banner')
