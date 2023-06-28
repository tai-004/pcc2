from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm, InstituicaoLoginForm, MenorForm, MenoresForm
from django.template import loader
from django.contrib.auth.models import User, Group
from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.dispatch import receiver
from accounts.models import Profile, Instituicao
from voluntariado.models import Voluntario
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, InstituicaoForm
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.views.generic import TemplateView
from responsavel.models import Responsavel
from voluntariado.models import Curriculo
from django.urls import resolve
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.forms import formset_factory
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from doacao.models import DoacaoCampanhaObj
#login e register#############################################################
from .forms import SearchForm


def search_users(request):

    instituicao = Instituicao.objects.all().order_by('nome')
    paginator = Paginator(instituicao, 2)
    page_number = request.GET.get('page')
    stream_data = paginator.get_page(page_number)

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            users = Instituicao.objects.filter(nome__icontains=search_query)
            return render(request, 'search_results.html', {'users': users})
    else:
        form = SearchForm() 

    context = {
    'instituicao': instituicao,
    'stream_data': stream_data,
    'form': form
    }
    return render(request, 'search.html', context)



def senhaDone(request):
    return render(request, 'change_password_done.html')



class redefinirSenha(PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_url = '/conta/recuperar/sucesso/'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = '/conta/recuperar/sucesso/'


#função que desativa o user / não apaga o user do bd.
def sairConta(request, id):
        user = get_object_or_404(User, id=id) #pega o id do usuario
        user.is_active = False  # verifica o id do user e define a conta como inativa
        user.save() #salva o user 

        return redirect("login") # retorna ao login
        
   
      
def responalert(request):
    return render(request, "registration/responsavel.html", {})


#define a pesquisa da instituição por parte do user comum.
def perfilInstituicao(request, username):
    user = get_object_or_404(User, username=username) #pega o user e username
   
    voluntario = Voluntario.objects.filter(user=user).order_by('-data')
    doacao = DoacaoCampanhaObj.objects.filter(user=user).order_by('-data')

    context = {
            'user': user,
            'voluntario': voluntario,
            'doacao': doacao
    }
    return render(request, 'registration/app-profile.html', context)


def perfil(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    template = loader.get_template('registration/apresenteprofile.html')

    context = {
        'profile':profile,

    }

    return HttpResponse(template.render(context, request))


#usuarios maiores de 18 anos/ sem responsavel / 
#tem a função de salvar o 'user' e adicionar no grupo desejado.
def UsuarioCreate(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save() #salva o formulario de usuario
            groupo = Group.objects.get(name='usuarios') #pega o  grupo 'usuarios'
            user.groups.add(groupo) # add o user no grupo selecionado
            return redirect('login') # retorna para a página de login
    else:
        form = UsuarioForm()
    return render(request, "registration/register.html", {'form': form}) 



#essa função é utilizada para salvar a idade do usuario permitindo separa-los em 'menores de 18' e 'maiores de 18'
def menoresIdade(request):
    if request.method == 'POST':
        form = MenoresForm(request.POST)
        if form.is_valid():
            idade = form.cleaned_data['idade'] #valida o campo idade
            form.save() # envia para o bd e salva o formulario
            if idade == 17: # condição que permite enviar menores para paginas especificas de cadastros 
                
                return  redirect('menor') #retorna a função de cadastro de user menores de 18

            elif idade == 15: 
                
                return  redirect('menor')
            elif idade == 16: 

                return  redirect('menor')
            else:
                return redirect('registrar')
          #  return redirect('registrar')
    else:
        form = MenoresForm()
    return render(request, "registration/manores.html", {'form': form})


#usuarios menor de 18.
#Crie uma função separada para usuarios menores de idade
def MenorCreate(request):
    if request.method == 'POST':
        form = MenorForm(request.POST)
        if form.is_valid():
            user = form.save()#salva o formulario de usuario
            groupo = Group.objects.get(name='menores') #pega o  grupo 'menores'
            user.groups.add(groupo) # add o user no grupo selecionado
            return redirect('login') # retorna para a página de login
    else:
        form = MenorForm()
    return render(request, "registration/menor.html", {'form': form})


#registro de instituicao


def InstituicaoCreate(request):
    if request.method == 'POST':
        form = InstituicaoLoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            groupo = Group.objects.get(name='instituicao')
            user.groups.add(groupo)
            return redirect('login')
    else:
        form = InstituicaoLoginForm()
    return render(request, "registration/registrarinstituicao.html", {'form': form})
    




#perfil########################
@login_required
def criarprofile(request):
            if request.method == 'POST':
                form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
                if form.is_valid():
                    form.save()
                    username = request.user.username
                    messages.success(request, f'{username}, perfil atualizado.')
                    return redirect('/home')
            else:
                form = ProfileForm(instance=request.user.profile)
            
            context = {
              'form':form
            }
            return render(request, 'registration/profile.html', context)

@login_required
@permission_required('accounts.inst')

def criarinstituicao(request):
    if request.method == 'POST':
        form = InstituicaoForm(request.POST, request.FILES, instance=request.user.instituicao)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Seu perfil foi criado!.')
            return redirect('/home')
    else:
        form = InstituicaoForm(instance=request.user.instituicao)
    context = {'form':form}
    return render(request, 'registration/instituicaoprofile.html', context)

@login_required
@permission_required('accounts.inst')
#ler perfil da instiuição
def lerprofile(request):
    return render(request, "registration/apresenteprofile.html", {})
@login_required
@permission_required('accounts.atual')
#ler perfil de usuario simples 
def lerperfil(request):
    return render(request, "registration/perfilapresente.html", {})

def profilealert(request):
    return render(request, "registration/profile1.html", {})

