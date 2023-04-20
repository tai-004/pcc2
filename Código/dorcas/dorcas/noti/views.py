from django.shortcuts import render, redirect
from django.shortcuts import render,  get_object_or_404
from noti.models import Notification, Tabela_notis
from instituicao.models import Tabela
from django.http import HttpResponseRedirect
from django.urls import reverse
from instituicao.forms import NovaTabelaForm
# Create your views here.

def noti(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date')


    context = {
        'notifications': notifications
    }

    return render(request, 'notifications.html', context)


def notiTabelar(request, noti_id):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date')


    context = {
        'notifications': notifications
    }

    return render(request, 'instituicao/novatabela.html', context)



def morrer(request):
    user = request.user
    tabela = Notification.objects.filter(user=user).order_by('-data')


    context = {
        'tabela': tabela
    }

    return render(request, 'notifications.html', context)


#def detalhar(request, noti_id):

#    notifi = Notification.objects.get(id=noti_id)
#    context = {
#        'notifi': notifi
#    }
    
 #   return render(request, 'noti/detalhar.html', context)


def detalhar(request, noti_id):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date')
    notifi= get_object_or_404(Notification, id=noti_id, user=user)

    context = {
        'notifi': notifi,
        'notifications': notifications
    }
    return render(request, "noti/detalhar.html", context)

def apresentar(request, notiTabelar_id):
    user = request.user
    tabelarnoti = TabelaNoti.objects.filter(user=user).order_by('-date')
    notifi= get_object_or_404(TabelaNoti, id=notiTabelar_id, user=user)

    context = {
        'notifi': notifi,
        'tabelarnoti': tabelarnoti
    }
    return render(request, "instituicao/noti.html", context)
