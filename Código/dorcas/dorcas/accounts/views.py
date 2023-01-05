from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm


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