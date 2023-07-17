from django.shortcuts import render
from voluntariado.forms import NewVoluntarioForm, NovoCurriculoForm, pesquisaForm, voluntarioForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Voluntario, Favo, Informar, Curriculo
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from doacao.models import DoacaoCampanhaObj
from django.contrib import messages



def pesquisa(request):
    termo = request.GET.get('termo')
    tipo = request.GET.get('tipo')

    if tipo == 'usuario':
        resultados = Voluntario.objects.filter(titulo__icontains=termo)
        return render(request, 'search_results.html')
    elif tipo == 'produto':
        resultados = Instituicao.objects.filter(nome__icontains=termo)
        return render(request, 'search_results.html')
    else:
        resultados = None

    return render(request,'voluntariado/volunt.html', {'resultados': resultados})


def pesquisaVoluntario(request):

    voluntario = Voluntario.objects.all().order_by('titulo')
    paginator = Paginator(instituicao, 2)
    page_number = request.GET.get('page')
    stream_data = paginator.get_page(page_number)

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            voluntario = form.cleaned_data['voluntario']
            users = Voluntario.objects.filter(titulo__icontains=voluntario)
            return render(request, 'voluntariado/resultadoPesquisa.html', {'users': users})
    else:
        form = SearchForm() 

    context = {
    'voluntario': voluntario,
    'stream_data': stream_data,
    'form': form
    }
    return render(request, 'voluntariado/volunt.html', context)

def cont(request):
    cont = None
    if request.user.is_authenticated:
        cont = Voluntario.objects.filter(user=request.user).count()
    return {'cont': cont}

   
@login_required 
@permission_required('voluntariado.inst')
def criarVoluntariar(request):
    if request.method == 'POST':
        form = NewVoluntarioForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("/accounts/perfil_instituicao/")
    else:
        form = NewVoluntarioForm()

    return render(request, "voluntariado/newpost.html", {"form": form})


#publica somente as vagas disponiveis do usuario 
def publicar(request):
    user = request.user
    voluntario = Voluntario.objects.filter(user=user).order_by('-data')
   
    return render(request, "voluntariado/publicar.html", {'voluntario': voluntario})


#posta todas as vagas de voluntariado disponivel(de todos os usuarios)
def postarTudo(request):

    voluntario = Voluntario.objects.all().order_by('-data')
    pesquisaVoluntario = Voluntario.objects.all().order_by('titulo')

    if request.method == 'GET':
        form = voluntarioForm(request.GET)
        if form.is_valid():
            voluntario = form.cleaned_data['voluntario']
            users = Voluntario.objects.filter(titulo__icontains=voluntario)
            return render(request, 'voluntariado/resultadoPesquisa.html', {'users': users})
    else:
        form = voluntarioForm() 
 
    context = {
    'voluntario': voluntario,
    'pesquisaVoluntario': pesquisaVoluntario,
    'form': form
    }
    return render(request, "voluntariado/volunt.html", context)



def notiCurriculo(request):
 
    curri = Curriculo.objects.all(Curriculo).order_by('-id')

    context = {
        'curri': curri
    }

    return render(request, "noti/detalhar2.html", context)


@login_required
def deletar(request, curriculo_id):
    user = request.user
    Curriculo.objects.filter(id=curriculo_id, user=user).delete()
    return redirect('mostrar')

 
@login_required
def atualizar(request, curriculo_id):
    user = request.user
    edit = Curriculo.objects.get(id=curriculo_id, user=user)
    form = NovoCurriculoForm(instance=edit)
    if form:
        if request.method == "POST":
                form = NovoCurriculoForm(request.POST, request.FILES, instance=edit)
                if form.is_valid():
                    form.save()
                    return redirect('mostar')
    
    else:
        return redirect('login')
    context = {
            'form': form,
            'edit' : edit
        }
    return render(request, 'voluntariado/curriculoEdit.html', context)

@login_required
@permission_required('voluntariado.inst')
def excluir(request, voluntario_id):
    user = request.user

    Voluntario.objects.filter(id=voluntario_id, user=user).delete()
   
    
    return redirect('publicarVolunt')

@login_required
@permission_required('voluntariado.inst')
def editar(request, voluntario_id):
    user = request.user
    edit = Voluntario.objects.get(id=voluntario_id, user=user)
    form = NewVoluntarioForm(instance=edit)
    if form:
        if request.method == "POST":
                form = NewVoluntarioForm(request.POST, request.FILES, instance=edit)
                if form.is_valid():
                    form.save()
                    return redirect('publicarVolunt')
    
    else:
        return redirect('login')
    context = {
            'form': form,
            'edit' : edit
        }
    return render(request, 'voluntariado/edit.html', context)

#resultado da viwes "favo"
def postCurtir(request, voluntario_id):
    user = request.user
    voluntario = get_object_or_404(Voluntario, id=voluntario_id)

    if Favo.objects.filter(voluntario=voluntario, user=user).exists():
        liked = True
    else:
        liked = False
    context = {
        'voluntario': voluntario,
        'liked': liked,
    }
 
    return render(request, 'voluntariado/vagas.html', context)

#o usuario favorita a vaga de voluntariado
@login_required
def favo(request, voluntario_id):
    user = request.user
    voluntario = get_object_or_404(Voluntario, id=voluntario_id)
    cfavo = voluntario.favoC

    favod = Favo.objects.filter(user=user, voluntario=voluntario).count()

    if not favod:
        favo = Favo.objects.create(user=user, voluntario=voluntario)
        cfavo = cfavo + 1
    else:
        Favo.objects.filter(user=user, voluntario=voluntario).delete()
        cfavo = cfavo - 1
    
    voluntario.favoC = cfavo
    voluntario.save()

   
    return HttpResponseRedirect(reverse('postlike', args=[voluntario_id]))


# mostra se o usuario foi aceito a vaga de voluntariado: resultado de "pedir"
def curtir(request, curriculo_id):
    user = request.user
    curriculo = get_object_or_404(Curriculo, id=curriculo_id)

    if Informar.objects.filter(curriculo=curriculo, user=user).exists():
        aceitar = True
    else:
        aceitar = False
    context = {
        'curriculo': curriculo,
        'aceitar': aceitar,
    }

    return render(request, 'voluntariado/curriculodetalhe.html', context)

@login_required
#a instituição aceita o usuario na vaga de volutariado e envia notificação para p/ o mesmo.
def pedir(request, curriculo_id):
    user = request.user
    curriculo = get_object_or_404(Curriculo, id=curriculo_id)
    cfavo = curriculo.aceitar_count

    favod = Informar.objects.filter(user=user, curriculo=curriculo).count()

    if not favod:
        favo = Informar.objects.create(user=user, curriculo=curriculo)
        cfavo = cfavo + 1
    
    
    curriculo.aceitar_count = cfavo
    curriculo.save()

   
    return HttpResponseRedirect(reverse('curtir', args=[curriculo_id]))


#perfil de curriculo do usuario
class CurriculoUpdate(UpdateView):
    template_name = "voluntariado/curriculo.html"
    model = Curriculo
    fields = ('data_nasc', 'telefone', 'email', 'tempo_disponivel', 'motivacao', 'resumo')
    success_url = reverse_lazy("templates")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Curriculo, user=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["titulo"] = "Meus dados pessoais"
        context["botao"] = "Atualizar"

        return context

def ntso(request, curriculo_id):
    curriculo = get_object_or_404(Curriculo, id=curriculo_id)
    context = {
        'curriculo': curriculo,
    }

    return render(request, 'notifications.html', context)
    
