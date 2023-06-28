from django.shortcuts import render, redirect
from django.shortcuts import render,  get_object_or_404
from noti.models import Notificacao, Tabela_notis
from instituicao.models import Tabela
from django.http import HttpResponseRedirect
from django.urls import reverse
from instituicao.forms import NovaTabelaForm
from voluntariado.models import Curriculo
from django.db.models import Count
from noti.forms import Tabela_notisForm
from django.contrib.auth.decorators import login_required

#função de avaliar o desempenho do voluntario
@login_required

def desempenho(request, tabela_notis_id):
    sender = request.user
    edita = Tabela_notis.objects.get(id=tabela_notis_id, sender=sender)
    form = Tabela_notisForm(instance=edita)
    if form:
        if request.method == "POST":
                form = Tabela_notisForm(request.POST, request.FILES, instance=edita)
                if form.is_valid():
                    form.save()
                    return redirect('tabela_notis')
    
    else:
        return redirect('login')
    context = {
            'form': form,
            'edita' : edita
        }
    return render(request, 'noti/notiPreencher.html', context)


#tem a função de contar as notificações não lidas do usuario
def countarNoti(request):
    contar = None
    somar = None
    if request.user.is_authenticated:
        contar = Notificacao.objects.filter(user=request.user, visto=False).count()
        somar = Tabela_notis.objects.filter(user=request.user, lido=False).count()
        som = contar + somar
    return {'contar': contar, 'somar': somar, 'som': som}

#deleta a notificação: função inativa
def apagar(request, noti_id):
    user = request.user
    Notificacao.objects.filter(id=noti_id, user=user).delete()
    return redirect('noti')

#apresenta  todas as notificações disponiveis para o usuario
def apresentaNoti(request):
    user = request.user
    notifications = Notificacao.objects.filter(user=user).order_by('-data')
    Notificacao.objects.filter(user=user, visto=False).update(visto=True)
    notiTabe = Tabela_notis.objects.filter(user=user).order_by('-data')


    context = {
        'notifications': notifications,
        'notiTabe': notiTabe,
    }

    return render(request, 'notifications.html', context)

#deve ser apagada: sem importancia
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


@login_required
#tabela de doação para user simples
def tabela_notis(request):
    sender = request.user


    tabela_notis = Tabela_notis.objects.filter(sender=sender).order_by('-data')
    
    context = {
    'tabela_notis': tabela_notis,
  
    }

    return render(request, "noti/tabela_notis.html", context)

def notiTabela(request):
    user = request.user
    notiTabe = Tabela_notis.objects.filter(user=user).order_by('-data')


    context = {
        'notiTabe': notiTabe
    }

    return render(request, 'notifica.html', context)


def detalhar(request, noti_id):
    user = request.user
    notifications = Notificacao.objects.filter(user=user).order_by('-data')
    notifi= get_object_or_404(Notificacao, id=noti_id, user=user)
    nto = Curriculo.objects.all().order_by('-id')
 
    
    context = {
        'notifi': notifi,
        'notifications': notifications,
        'nto': nto
      

    }
    return render(request, "noti/detalhar2.html", context)


def nnn(request):
    user = request.user
    voluntario = Curriculo.objects.filter(user=user)
   
    return render(request, "noti.html", {'voluntario': voluntario})
    

