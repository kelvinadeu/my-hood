from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login
from django.http import HttpResponse


def article(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()

    return render(request,'registration_form.html',locals())

def profile(request,user_id):
    user_id = request.user
    profile = Profile.objects.get(user=current_user.id)
    return render (request, 'profile/profile.html',{"profile":profile,"hoods":hoods})

def edit_profile(request):
    user_id = rquest.user
    profile = Profile.objects.get(user=user_id)
    if request.method == 'POST':
        registration_form = EditForm(request.POST, request.Files,insatnce=request.user.profile)
        if registration_form.is_valid():
            registration_form.save()
            return redirect('profile')
    else:
        registration_form = EditForm()
    return render(request, 'profile/edit_profile.html', {"form":registration_form,"profile":profile})                
