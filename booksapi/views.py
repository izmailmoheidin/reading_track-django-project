from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BooK
from .forms import creationUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def index(request):
    books = BooK.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'index.html',context )


def registerPage(request):
    form = creationUserForm()
    
    if request.method == 'POST':
        form = creationUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'account was created '+ user)
            return redirect('login')
        
    context = {'form': form}
    return render(request, 'registerForm.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate (request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'username OR password is incorrect')
    context = {}
    return render(request , 'login.html', context)
    
def logoutPage(request):
    logout(request)
    return redirect ('login') 
          