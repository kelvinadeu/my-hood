from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.http import Http404
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm


def home(request):
    all_hoods = Hood.objects.all()
    return render(request, 'home.html', locals())

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()

    return render(request,'signup.html',locals())

def profile(request,user_id):
    user_id = request.user
    profile = Profile.objects.get(user=request_user_id)
    return render (request, 'profile/profile.html',{"profile":profile,"hoods":hoods,"user_id":user_id})
@login_required(login_url='/accounts/login')
def edit_profile(request):
    user_id = rquest.user
    profile = Profile.objects.get(user=user_id)
    if request.method == 'POST':
        registration_form = EditForm(request.POST, request.Files,insatnce=request.user_id.profile)
        if registration_form.is_valid():
            registration_form.save()
            return redirect('profile')
    else:
        registration_form = EditForm()
    return render(request, 'profile/edit_profile.html', {"form":registration_form,"profile":profile})

@login_required(login_url='/accounts/login')
def add_business(request):

    current_user = request.user
    form=BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = BusinessForm.save()
            business.name= current_user
            business.save()
            return redirect('home')
    else:
        form = BusinessForm()
    return render(request,'add-business.html',{'form': form})
