
from django.shortcuts import redirect
from responsavel.forms import ResponsavelForm
from responsavel.models import Responsavel
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404


def EditResponsavel(request):
   
    if request.method == 'POST':
        form = ResponsavelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("login")
    else:
       form = ResponsavelForm()

    return render(request, 'responsavel/responsavel.html', {"form": form})


#def EditResponsavel(request):
    #user = request.user.id
    #responsavel = Responsavel.objects.get(user__id=user)
    #responsavel = User.objects.get(id=user)
    ##if request.method == 'POST':
      #  form = ResponsavelForm(request.POST, request.FILES, instance=responsavel)
       # if form.is_valid():
        #    responsavel.nome = form.cleaned_data.get('nome')
         #   responsavel.parentesco = form.cleaned_data.get('parentesco')
          #  responsavel.telefone = form.cleaned_data.get('telefone')
           # responsavel.idade = form.cleaned_data.get('idade')
            #responsavel.cidade = form.cleaned_data.get('cidade')
            #responsavel.rua = form.cleaned_data.get('rua')
            #responsavel.numero = form.cleaned_data.get('numero')
      #      responsavel.bairro = form.cleaned_data.get('bairro')
     #       responsavel.cpf = form.cleaned_data.get('cpf')
       #     responsavel.save()
           
        #    return redirect('login')
   # else:
    #    form = ResponsavelForm(instance=responsavel)

    context={
        'form':form,
    }

    return render(request, 'responsavel/responsavel.html', context)