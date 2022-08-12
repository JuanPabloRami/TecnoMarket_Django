from math import prod
from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from cgitb import text
from .models import Producto
from .forms import ContactoForm, ProductoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.

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


def agregarProducto(request):
    data = {
        "form": ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,files =request.FILES)
        if formulario.is_valid:
            formulario.save()
            messages.success(request,"¡Producto Creado correctamente!")
            return redirect(to='listarProducto')
        else:
            data["form"]= formulario

    
    return render(request,'producto/agregar.html', data)


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

def eliminarProducto(request,id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request,"Producto eliminado correctamente")
    return redirect(to='listarProducto')

