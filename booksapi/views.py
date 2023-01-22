from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BooK
from .forms import creationUserForm, BookForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# index veiw
@login_required(login_url='login')
def index(request):
    books = BooK.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'index.html',context )

# regster view
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

# login veiw
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

def createBook(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid:
            form.save()
            
    context={'form': form}
    return render(request , 'createBook.html',context )

def bookUpdate(request, pk):
    book = BooK.objects.get(bookId=pk)
    form = BookForm(instance=book)
    
    if request.method == 'POST':
        form = BookForm(request.POST,instance=book )
        if form.is_valid:
            form.save()
            return redirect('index') 
    context={'form': form}
    return render(request , 'createBook.html',context )

def deleteBook(request, pk):
    book = BooK.objects.get(bookId=pk),
    if request.method=='POST':
        book.delete()
        return redirect('index') 
        
        
    
    context={'item': book}
    return render(request ,  "delete.html", context)
    
          