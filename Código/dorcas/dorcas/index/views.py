from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def templates(request):
    return render(request, "index.html", {})



def dorcas(request):
    return render(request, "dorcas.html", {})

