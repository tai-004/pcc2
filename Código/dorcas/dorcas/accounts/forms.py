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

class SearchForm(forms.Form):
    search_query = forms.CharField(label='Digite o nome da instituição')

class MenorForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
   # idade = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'password1', 'password2']

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError("O email {} já está em uso.".format(e))

        return e 

    #def clean_cpf(self):
     #   c = self.cleaned_data['idade']
      #  if idade < 15:
       #     raise ValidationError("buu")

       # if User.objects.filter(cpf=c).exists():
        #    raise ValidationError("O cpf {} já está em uso.".format(c))

        #return c   
    

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
  #  username = forms.CharField(widget=forms.TextInput(), max_length=30, required=True)
  #  idade = forms.IntegerField()
 
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'password1', 'password2']
    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError("O email {} já está em uso.".format(e))

        return e
   # def clean_username(self):
    #    u = self.cleaned_data['username']
     #   if User.objects.filter(username=u).exists():
      #      raise ValidationError("O username {} já está em udddddddso.".format(u))

       # return u

    #def clean_idade(self):
     #   ida = self.cleaned_data['idade']
      #  if ida <= 14 :
       #     raise ValidationError("Você não pode se cadastrar, tem idade inferior há 15 anos.".format(ida))
        
        #elif ida == 15 :
         #   raise ValidationError("Você precisa de um responsavel.".format(ida))
        #elif ida == 16 :
         #   raise ValidationError("Você precisa de um responsavel.".format(ida))
        #elif ida == 17 :

          #  raise ValidationError("Você precisa de um responsavel.".format(ida))
         #   
       # return ida


class MenoresForm(ModelForm):
  #  campo = forms.CharField()
    idade = forms.IntegerField()
    #def clean(self):
     #   cleaned_data = super().clean()
    #    cpf = cleaned_data.get('campo')

        # Realize a consulta ao banco de dados
     #   resultados = Profile.objects.filter(cpf=cpf)

        # Faça o processamento dos resultados conforme necessário
      #  for resultado in resultados:
       #     raise ValidationError("cpf em uso.".format(resultados))

        #return cleaned_data
 
 
    class Meta:
        model = Menores
        fields = ['idade']
   

    def clean_idade(self):
        ida = self.cleaned_data['idade']
        if ida <= 14 :
            raise ValidationError("Você não pode se cadastrar, tem idade inferior a 15 anos.".format(ida))
        
      #  elif ida == 15 :
       #     raise ValidationError("Você precisa de um responsavel.".format(ida))
        #elif ida == 16 :
         #   raise ValidationError("Você precisa de um responsavel.".format(ida))
    #    elif ida == 17 :

     #       raise ValidationError("Você precisa de um responsavel.".format(ida))
            
        return ida

    
 

class InstituicaoLoginForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username','last_name', 'first_name', 'email', 'password1', 'password2']

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
         'banner': FileInput(),
         }
        
