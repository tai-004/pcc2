from django.shortcuts import render, redirect
from django.shortcuts import render,  get_object_or_404
from noti.models import Notificacao
from instituicao.models import Tabela
from django.http import HttpResponseRedirect
from django.urls import reverse
from instituicao.forms import NovaTabelaForm
# Create your views here.

def apresentaNoti(request):
    user = request.user
    notifications = Notificacao.objects.filter(user=user).order_by('-data')


    context = {
        'notifications': notifications
    }

    return render(request, 'notifications.html', context)


def notiTabelar(request, noti_id):
    user = request.user
    notifications = Notificacao.objects.filter(user=user).order_by('-data')


    context = {
        'notifications': notifications
    }

    return render(request, 'instituicao/novatabela.html', context)



def apresentaNoti2(request):
    user = request.user
    tabela = Notificacao.objects.filter(user=user).order_by('-data')


    context = {
        'tabela': tabela
    }

    return render(request, 'notifications.html', context)


def detalhar(request, noti_id):
    user = request.user
    notifications = Notificacao.objects.filter(user=user).order_by('-data')
    notifi= get_object_or_404(Notificacao, id=noti_id, user=user)

    context = {
        'notifi': notifi,
        'notifications': notifications
    }
    return render(request, "noti/detalhar.html", context)

#def apresentar(request, notiTabelar_id):
  #  user = request.user
 #   tabelarnoti = TabelaNoti.objects.filter(user=user).order_by('-data')
   # notifi= get_object_or_404(TabelaNoti, id=notiTabelar_id, user=user)

    #context = {
     #   'notifi': notifi,
      #  'tabelarnoti': tabelarnoti
    #}
    #return render(request, "instituicao/noti.html", context)
