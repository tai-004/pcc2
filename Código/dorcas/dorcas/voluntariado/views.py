from django.shortcuts import render
from voluntariado.forms import NewVoluntarioForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Voluntario, Likes
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse



@login_required
@permission_required('voluntariado.inst')
def NewVoluntario(request):
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

def postlike(request, voluntario_id):
    user = request.user
    voluntario = get_object_or_404(Voluntario, id=voluntario_id)

    if Likes.objects.filter(voluntario=voluntario, user=user).exists():
        liked = True
    else:
        liked = False
    context = {
        'voluntario': voluntario,
        'liked': liked,
    }

    return render(request, 'voluntariado/publica.html', context)


def posttudo(request):
 
    voluntario = Voluntario.objects.all().order_by('-date')
   
    return render(request, "home.html", {'voluntario': voluntario})


@login_required
@permission_required('voluntariado.inst')
def excluir(request, voluntario_id):
    user = request.user
    Voluntario.objects.filter(id=voluntario_id, user=user).delete()
    return redirect('publicar')


@login_required

@permission_required('voluntariado.inst')
def editar(request, voluntario_id):
    edit = Voluntario.objects.get(id=voluntario_id)
    form = NewVoluntarioForm(instance=edit)

    if request.method == "POST":
        form = NewVoluntarioForm(request.POST, request.FILES, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('publicar')
        
    context = {
            'form': form,
            'edit' : edit
        }
    return render(request, 'voluntariado/edit.html', context)


@login_required
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


def like(request, voluntario_id):
    user = request.user
    post = get_object_or_404(Voluntario, id=voluntario_id)
    current_likes = post.likes_count

    liked = Likes.objects.filter(user=user, post=post).count()

    if not liked:
        like = Likes.objects.create(user=user, post=post)
        current_likes = current_likes + 1
    else:
        Likes.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
    
    post.likes_count = current_likes
    post.save()

    return HttpResponseRedirect(reverse('postlike', args=[post_id]))
