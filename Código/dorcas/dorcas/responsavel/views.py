from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from responsavel.forms import ResponsavelForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Responsavel
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render,  get_object_or_404


def sponsavel(request):
    if request.method == 'POST':
        form = ResponsavelForm(request.POST)
        if form.is_valid():
            form.save() #salva o formulario de usuario
            
            return redirect('templates') # retorna para a página de login
    else:
        form = ResponsavelForm()
    return render(request, "responsavel/newpost.html", {'form': form}) 

class newresponsavel(UpdateView):
    template_name = "responsavel/newpost.html"
    model = Responsavel
    fields = ("nome", "idade", "parentesco", "cpf", "cidade", "rua", "numero", "bairro", "telefone")
    success_url = reverse_lazy("templates")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Responsavel, user=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["titulo"] = "Meus dados pessoais"
        context["botao"] = "Atualizar"

        return context

#class newresponsavel(UpdateView):
 #   if request.method == 'POST':
  #      form = ResponsavelForm(request.POST)
   #     if form.is_valid():
    #        post = form.save(commit=False)
     #       post.user = request.user
      #      post.save()
       #     return redirect('/home')
#    else:
 #       form = ResponsavelForm()

  #  return render(request, 'responsavel/newpost.html', {"form": form})


def publicar(request):
    user = request.user
    responsavel = Responsavel.objects.filter(user=user)
   
    return render(request, "responsavel/responsavel.html", {'responsavel': responsavel})

def detalhar(request,id):
    user = request.user
    notifications = Responsavel.objects.filter(user=user)
    responsavel= get_object_or_404(Responsavel, pk=id, user=user)

    context = {
        'responsavel': responsavel,
        'notifications': notifications
    }
    return render(request, "responsavel/responsavel.html", context)
