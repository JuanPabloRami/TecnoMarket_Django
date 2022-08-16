from math import prod
from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from cgitb import text
from .models import Producto,Marca
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer,MarcaSerializer

# Create your views here.

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = Producto.objects.all()
        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre__contains = nombre)

        return productos


def errorFacebook(request):
    return render(request,'registration/errorFacebook.html')


def index(request):
    productos = Producto.objects.all()
    data= {
        "productos":productos
    }
    return render(request,'index.html',data)

def contacto(request):
    data={
        'form':ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "¡Se ha guardado tu mensaje!"
        else:
            data["form"] = formulario
    return render(request,'contacto.html',data)

def galeria(request):
    return render(request,'galeria.html')

@permission_required('app.add_producto')
def agregarProducto(request):
    data = {
        "form": ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,files =request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"¡Producto Creado correctamente!")
            return redirect(to='listarProducto')
        else:
            data["form"]= formulario

    
    return render(request,'producto/agregar.html', data)

@permission_required('app.view_producto')
def listarProducto(request):
    productos = Producto.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(productos,5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        "entity":productos,
        "paginator":paginator
    }
    return render(request,'producto/listar.html', data)

@permission_required('app.change_producto')
def modificarProducto(request,id):
    producto = get_object_or_404(Producto, id=id)

    data ={
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance= producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto modificado correctamente")
            return redirect(to='listarProducto')
        data["form"] = formulario

    return render(request,'producto/modificar.html',data)

@permission_required('app.delete_producto')
def eliminarProducto(request,id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request,"Producto eliminado correctamente")
    return redirect(to='listarProducto')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html',data)

