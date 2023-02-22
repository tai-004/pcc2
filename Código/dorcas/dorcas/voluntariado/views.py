from django.shortcuts import render
from voluntariado.forms import NewVoluntarioForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Voluntario

@login_required
def NewVoluntario(request):
    if request.method == 'POST':
        form = NewVoluntarioForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("/informes/post/")
    else:
        form = NewVoluntarioForm()

    return render(request, "voluntariado/newpost.html", {"form": form})



def DetalharPost(request, id):
    voluntario = Voluntario.objects.get(pk=id)
    context = {
        'voluntario': voluntario
    }
    
    return render(request, 'voluntariado/vagas.html', context)


def publicar(request):
    list_filter = Voluntario.objects.order_by('titulo').filter(titulo=True)
    
    if 'publicar' in request.GET:
        nome = request.GET['publicar']
        if nome:
            list_filter = list_filter.filter(titulo__icontains=nome)

    return render(request, 'voluntariado/publicar.html', {'files': list_filter})