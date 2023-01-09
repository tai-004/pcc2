
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm
from django.template import loader
from accounts.forms import EditProfileForm
from django.contrib.auth.models import User
from accounts.models import Profile
from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse




class UsuarioCreate(CreateView):
    template_name = "registration/register.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"

        return context


def UserProfile(request, username):
	user = get_object_or_404(User, username=username)
	profile = Profile.objects.get(user=user)

	template = loader.get_template('registration/profile.html')

	context = {
		'profile':profile,

	}

	return HttpResponse(template.render(context, request))


def EditProfile(request):
	user = request.user.id
	profile = Profile.objects.get(user__id=user)
	user_basic_info = User.objects.get(id=user)

	if request.method == 'POST':
		form = EditProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			profile.picture = form.cleaned_data.get('picture')
			profile.banner = form.cleaned_data.get('banner')
			profile.nome = form.cleaned_data.get('nome')
			profile.telefone = form.cleaned_data.get('telefone')
			profile.formacao = form.cleaned_data.get('formacao')
			profile.sexo = form.cleaned_data.get('sexo')
			profile.idade = form.cleaned_data.get('idade')
			profile.trabalho = form.cleaned_data.get('trabalho')
			profile.habilidades = form.cleaned_data.get('habilidades')
			profile.cidade = form.cleaned_data.get('cidade')
			profile.estado = form.cleaned_data.get('estado')
			profile.rua = form.cleaned_data.get('rua')
			profile.numero = form.cleaned_data.get('numero')
			profile.bairro = form.cleaned_data.get('bairro')
			profile.cpf = form.cleaned_data.get('cpf')   
			profile.save()
			user_basic_info.save()
			return redirect('login')
	else:
		form = EditProfileForm(instance=profile)

	context={
		'form':form,
	}

	return render(request, 'registration/editarperfil.html', context)