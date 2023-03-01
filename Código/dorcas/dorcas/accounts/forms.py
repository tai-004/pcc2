from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from .models import Profile, Instituicao
from django.forms.widgets import FileInput
from django.forms.models import ModelForm




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

class InstituicaoForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        ins = self.cleaned_data['email']
        if User.objects.filter(email=ins).exists():
            raise ValidationError("O email {} já está em uso.".format(ins))

        return ins



#class de formulario referente ao perfil do user comum
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
         'picture': FileInput(),
         }


#class de formulario referente ao perfil do user comum
class InstituicaoForm(ModelForm):
    class Meta:
        model = Instituicao
        fields = '__all__'
        exclude = ['user']
        widgets = {
         'picture': FileInput(),
         'banner': FileInput(),
         }
        
