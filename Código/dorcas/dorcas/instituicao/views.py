from django.shortcuts import render
from instituicao.forms import NovaTabelaForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Tabela
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse



def lertabelar(request):
    user = request.user
    tabelares = Tabela.objects.filter(user=user).order_by('-data')


    context = {
        'tabelares': tabelares
    }

    return render(request, 'instituicao/noti.html', context)