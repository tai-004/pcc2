
from django.shortcuts import redirect
from responsavel.forms import ResponsavelForm
from django.shortcuts import render
from django.shortcuts import redirect




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
