from django.shortcuts import render
from instituicao.forms import NovaTabelaForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Tabela
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse



#def novaTabelar(request):
 #   if request.method == 'POST':
  #      form = NovaTabelaForm(request.POST)
   #     if form.is_valid():
    #        tabela = form.save(commit=False)
     #       tabela.user = request.user
      #      tabela.save()
       #     return redirect("/accounts/apresenteprofile/")
  #  else:
   #     form = NovaTabelaForm()
#
 #   return render(request, "instituicao/novatabela.html", {"form": form})




def tabelar(request):
    user = request.user
    tabelares = Tabela.objects.filter(user=user).order_by('-data')


    context = {
        'tabelares': tabelares
    }

    return render(request, 'instituicao/noti.html', context)