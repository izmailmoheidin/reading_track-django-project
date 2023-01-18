from django.shortcuts import render
from django.http import HttpResponse
from .models import BooK

# Create your views here.
def index(request):
    books = BooK.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'index.html',context )
