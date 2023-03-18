from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from responsavel.forms import ResponsavelForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import permission_required


@login_required
@permission_required('accounts.atual')
def newresponsavel(request):
    if request.method == 'POST':
        form = ResponsavelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/accounts/profile')
    else:
        form = ResponsavelForm()

    return render(request, 'responsavel/newpost.html', {"form": form})
