from django.http import HttpResponse
from django.shortcuts import render
from cgitb import text

# Create your views here.

def index(request):
    return render(request,'index.html')

def contacto(request):
    return render(request,'contacto.html')

def galeria(request):
    return render(request,'galeria.html')


