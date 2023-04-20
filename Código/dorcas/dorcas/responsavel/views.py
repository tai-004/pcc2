from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from responsavel.forms import ResponsavelForm
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Responsavel
from django.contrib.auth.decorators import permission_required


@login_required
@permission_required('accounts.atual')
def newresponsavel(request):
    if request.method == 'POST':
        form = ResponsavelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/accounts/profile')
    else:
        form = ResponsavelForm()

    return render(request, 'responsavel/newpost.html', {"form": form})


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
