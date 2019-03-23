from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def article(request):
    return render(request, 'base.html')
