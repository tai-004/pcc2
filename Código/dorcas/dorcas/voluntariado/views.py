from django.shortcuts import render
from voluntariado.forms import NewVoluntarioForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Voluntario, BlogPost, Favo, Informar
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView


@login_required
@permission_required('voluntariado.inst')
def NovoVoluntariar(request):
    if request.method == 'POST':
        form = NewVoluntarioForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("/accounts/apresenteprofile/")
    else:
        form = NewVoluntarioForm()

    return render(request, "voluntariado/newpost.html", {"form": form})


def publicar(request):
    user = request.user
    voluntario = Voluntario.objects.filter(user=user).order_by('-date')
   
    return render(request, "voluntariado/publicar.html", {'voluntario': voluntario})


def postarTudo(request):
 
    voluntario = Voluntario.objects.all().order_by('-date')
   
    return render(request, "voluntariado/volunt.html", {'voluntario': voluntario})


@login_required
@permission_required('voluntariado.inst')
def excluir(request, voluntario_id):
    user = request.user
    Voluntario.objects.filter(id=voluntario_id, user=user).delete()
    return redirect('publicar')

 
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
                    return redirect('publicar')
    
    else:
        return redirect('login')
    context = {
            'form': form,
            'edit' : edit
        }
    return render(request, 'voluntariado/edit.html', context)

#@login_required
#def like(request, voluntario_id):
 #   user = request.user
 #   voluntario = get_object_or_404(Voluntario, id=voluntario_id)
 #   current_likes = voluntario.likes_count

  #  liked = Likes.objects.filter(user=user, voluntario=voluntario).count()

   # if not liked:
    #    like = Likes.objects.create(user=user, voluntario=voluntario)
     #   current_likes = current_likes + 1
   # else:
    #    Likes.objects.filter(user=user, voluntario=voluntario).delete()
     #   current_likes = current_likes - 1
    
    #voluntario.likes_count = current_likes
    #post.save()

    #return HttpResponseRedirect(reverse('postlike', args=[voluntario_id]))


#def like(request, voluntario_id):
#    user = request.user
 #   voluntario = get_object_or_404(Voluntario, id=voluntario_id)
  #  current_likes = Voluntario.likes_count

   # liked = Likes.objects.filter(user=user, voluntario=voluntario).count()

    #if not liked:
     #   like = Likes.objects.create(user=user, voluntario=voluntario)
      #  current_likes = current_likes + 1

    
    #voluntario.likes_count = current_likes
    #voluntario.save()

    #return HttpResponseRedirect(reverse('postlike', args=[voluntario_id]))

def postlike(request, voluntario_id):
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



def curtir(request, voluntario_id):
    user = request.user
    voluntario = get_object_or_404(Voluntario, id=voluntario_id)

    if Informar.objects.filter(voluntario=voluntario, user=user).exists():
        aceitar = True
    else:
        aceitar = False
    context = {
        'voluntario': voluntario,
        'aceitar': aceitar,
    }

    return render(request, 'voluntariado/vagas.html', context)

@login_required
def pedir(request, voluntario_id):
    user = request.user
    voluntario = get_object_or_404(Voluntario, id=voluntario_id)
    cfavo = voluntario.aceitar_count

    favod = Informar.objects.filter(user=user, voluntario=voluntario).count()

    if not favod:
        favo = Informar.objects.create(user=user, voluntario=voluntario)
        cfavo = cfavo + 1
    
    
    voluntario.aceitar_count = cfavo
    voluntario.save()

   
    return HttpResponseRedirect(reverse('curtir', args=[voluntario_id]))






    #return render(request, "voluntariado/volunt.html", {'voluntario': voluntario_id})

