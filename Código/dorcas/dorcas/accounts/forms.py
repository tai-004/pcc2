from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import  Group
from django.shortcuts import render,  get_object_or_404
from responsavel.models import Responsavel
from .models import Profile, Instituicao, Menores
from django.forms.widgets import FileInput
from django.forms.models import ModelForm
from accounts.models import Profile

#pesquisa a instituição
class SearchForm(forms.Form):
    search_query = forms.CharField(label='Digite o nome da instituição')

#valida o formulario de menores de idade com email
class MenorForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
 
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'password1', 'password2']

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError("O email {} já está em uso.".format(e))

        return e 

    
    

#valida o formulario de usuario  com email
class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError("O email {} já está em uso.".format(e))

        return e
  


#formulario ue pergunta idade do user antes do login
class MenoresForm(ModelForm):
    idade = forms.IntegerField()

    class Meta:
        model = Menores
        fields = ['idade']
   

    def clean_idade(self):
        ida = self.cleaned_data['idade']
        if ida <= 14 :
            raise ValidationError("Você não pode se cadastrar, tem idade inferior a 15 anos.".format(ida))
        
      
            
        return ida

    
 
    
 

#valida o formulario dda instituição com email
class InstituicaoLoginForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

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
        'banner': FileInput(),
         }


#class de formulario referente ao perfil do user comum
class InstituicaoForm(ModelForm):
    class Meta:
        model = Instituicao
        fields = '__all__'
        exclude = ['user']
        widgets = {
         'picture': FileInput(),
         }
        
