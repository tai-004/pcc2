from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms



class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100) #tamanho do email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #parametros para o login

    def clean_email(self):  #validação de email
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError("O email {} já está em uso.".format(e))

        return e
