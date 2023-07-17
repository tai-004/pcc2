from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import DoacaoCampanhaObj, DoacaoCampanhaDinheiro, DoeUser, TabelarDoe
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from doacao.forms import DoacaoCampanhaObjForm, DoacaoCampanhaDinheiroForm, DoacaoCampanhaObjUserForm
from django.contrib import messages


#cria a campanha de doação de objetos(ator: instituição)
@login_required
@permission_required('doacao.doacao')
def criarDoacaoCampanhaObj(request):
    if request.method == 'POST':
        form = DoacaoCampanhaObjForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("/accounts/perfil_instituicao/")
    else:
        form = DoacaoCampanhaObjForm()
    context = {
    "form": form
    }

    return render(request, "doacao/criar.html", context)


#posta todas as vagas de doações disponivel(de todos os usuarios)
def postarDoacao(request):
    doacao = DoacaoCampanhaObj.objects.all().order_by('-data')
    dinheiro = DoacaoCampanhaDinheiro.objects.all().order_by('-data')

    context = {
    'doacao': doacao,
    'dinheiro': dinheiro
    }

    return render(request, "doacao/postarTodas.html", context)

#postas todas as minhas campanhas
def publicarDoacao(request):
    user = request.user
    doacao = DoacaoCampanhaObj.objects.filter(user=user).order_by('-data')
    dinheiro = DoacaoCampanhaDinheiro.objects.filter(user=user).order_by('-data')
    
    context = {
    'doacao': doacao,
    'dinheiro': dinheiro
    }

    return render(request, "doacao/publicar.html", context)

#deleta campanhas de doações
@login_required
@permission_required('doacao.doacao')
def deletar(request, doacaocampanhaobj_id):
    user = request.user
    DoacaoCampanhaObj.objects.filter(id=doacaocampanhaobj_id, user=user).delete()
    return redirect('publicar')


#atualiza a doação (somente os donos do post: instituição)
@login_required
@permission_required('doacao.doacao')
def atualizar(request, doacaocampanhaobj_id):
    user = request.user
    edita = DoacaoCampanhaObj.objects.get(id=doacaocampanhaobj_id, user=user)
    form = DoacaoCampanhaObjForm(instance=edita)
    if form:
        if request.method == "POST":
                form = DoacaoCampanhaObjForm(request.POST, request.FILES, instance=edita)
                if form.is_valid():
                    form.save()
                    return redirect('postarDoacao')
    
    else:
        return redirect('login')
    context = {
            'form': form,
            'edita' : edita
        }
    return render(request, 'doacao/editar.html', context)

###################################################################

#Doação dinheiro

#cria a campanha de doação de dinheiro(ator: instituição)
@login_required
@permission_required('doacao.chave')
def criarDoacaoCampanhaDinheiro(request):
    if request.method == 'POST':
        form = DoacaoCampanhaDinheiroForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("/accounts/perfil_instituicao")
    else:
        form = DoacaoCampanhaDinheiroForm()
    context = {
    "form": form
    }

    return render(request, "doacao/criarDinheiro.html", context)



#postas todas as minhas campanhas 
def publicarDoacaoDinheiro(request):
    user = request.user
    dinheiro = DoacaoCampanhaDinheiro.objects.filter(user=user).order_by('-data')
    context = {
    'dinheiro': dinheiro
    }

    return render(request, "doacao/publicar.html", context)

#deleta campanhas de doações de dinheiro
@login_required
@permission_required('doacao.chave')
def excluir(request, doacaocampanhadinheiro_id):
    user = request.user
    DoacaoCampanhaDinheiro.objects.filter(id=doacaocampanhadinheiro_id, user=user).delete()
    return redirect('publicar')
   


#atualiza a doação de dinheiro (somente os donos do post: instituição)
@login_required
@permission_required('doacao.chave')
def editar(request, doacaocampanhadinheiro_id):
    user = request.user
    edita = DoacaoCampanhaDinheiro.objects.get(id=doacaocampanhadinheiro_id, user=user)
    form = DoacaoCampanhaDinheiroForm(instance=edita)
    if form:
        if request.method == "POST":
                form = DoacaoCampanhaDinheiroForm(request.POST, request.FILES, instance=edita)
                if form.is_valid():
                    form.save()
                    return redirect('publicar')
    
    else:
        return redirect('login')
    context = {
            'form': form,
            'edita' : edita
        }
    return render(request, 'doacao/editarPix.html', context)

#################################################



  
#tabela de doação para user simples
def tabelaDoacaoUser(request):
    sender = request.user
    tabela = DoeUser.objects.filter(sender=sender).order_by('-data')
    
    context = {
    'tabela': tabela,
  
    }

    return render(request, "doacao/tabela.html", context)

#tabela de doação para instituição
def tabelaDoacaoInst(request):
    user = request.user
    tabela = DoeUser.objects.filter(user=user).order_by('-data')
    
    context = {
    'tabela': tabela,
  
    } 

    return render(request, "doacao/tabelaInst.html", context)


##############################################

#reação de pedir
def doar(request, doacaocampanhaobj_id):
    user = request.user
    doacao = get_object_or_404(DoacaoCampanhaObj, id=doacaocampanhaobj_id)

    if TabelarDoe.objects.filter(doacao=doacao, user=user).exists():
        aceitar = True
    else:
        aceitar = False
    context = {
        'doacao': doacao,
        'aceitar': aceitar,
    } 

    return render(request, 'doacao/doacaoPedir.html', context)

#realiza a notificação de querer doar
@login_required
def pedir(request, doacaocampanhaobj_id):
    user = request.user
    doacao = get_object_or_404(DoacaoCampanhaObj, id=doacaocampanhaobj_id)
    cont = doacao.cont

    favod = TabelarDoe.objects.filter(user=user, doacao=doacao).count()

    if not favod:
        favo = TabelarDoe.objects.create(user=user, doacao=doacao)
        cont = cont + 1
    
    
    doacao.cont = cont
    doacao.save()

   
    return HttpResponseRedirect(reverse('doar', args=[doacaocampanhaobj_id]))

#edita a data e quantidade de doação
def doeEdit(request, doeuser_id):
    sender = request.user
    edita = DoeUser.objects.get(id=doeuser_id, sender=sender)
    form = DoacaoCampanhaObjUserForm(instance=edita)
    if form:
        if request.method == "POST":
                form = DoacaoCampanhaObjUserForm(request.POST, request.FILES, instance=edita)
                if form.is_valid():
                    form.save()
                    return redirect('tabelaDoacao')
    
    else:
        return redirect('login')
    context = {
            'form': form,
            'edita' : edita
        }
    return render(request, 'doacao/notiEdit.html', context)
