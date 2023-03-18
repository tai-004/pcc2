from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm, InstituicaoForm
from django.template import loader
from django.contrib.auth.models import  Group
from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.dispatch import receiver
from accounts.models import Profile, Instituicao
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, InstituicaoForm
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.views.generic import TemplateView

#login e register#############################################################################################

def UserProfile(request, username):
	user = get_object_or_404(User, username=username)
	profile = Profile.objects.get(user=user)
	template = loader.get_template('profile.html')

	context = {
		'profile':profile,

	}

	return HttpResponse(template.render(context, request))

#registro de usuario comum
class UsuarioCreate(CreateView):
    template_name = "registration/register.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="usuarios")
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"

        return context
    

#registro de instituicao
class InstituicaoCreate(CreateView):
    template_name = "registration/registrarinstituicao.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        url = super().form_valid(form)
        grupo = get_object_or_404(Group, name="instituicao")
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"

        return context
#########################################################################################



#perfil########################
@login_required
def profile(request):
            if request.method == 'POST':
                form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
                if form.is_valid():
                    form.save()
                    username = request.user.username
                    messages.success(request, f'{username}, Your profile is updated.')
                    return redirect('/home')
            else:
                form = ProfileForm(instance=request.user.profile)
            context = {'form':form}
            return render(request, 'registration/profile.html', context)

@login_required
@permission_required('accounts.inst')

def instituicao(request):
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

def apresenteprofile(request):
    return render(request, "registration/apresenteprofile.html", {})



def profilealert(request):
    return render(request, "registration/profile1.html", {})



