from django import forms
from .models import Voluntario
from django.forms.widgets import FileInput
from django.contrib.auth.forms import User


class NewVoluntarioForm(forms.ModelForm):
     class Meta:
        model = Voluntario
        fields = '__all__'
        exclude = ['user']
        widgets = {
         'picture': FileInput(),
         }