from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('contacto/',views.contacto,name='contacto'),
    path('galeria/',views.galeria,name='galeria'), 
    path('agregar-producto/',views.agregarProducto,name='agregarProducto'),
    path('listar-producto/',views.listarProducto,name='listarProducto'),
    path('modificar-producto/<id>/',views.modificarProducto,name='modificarProducto'),
    path('eliminar-producto/<id>/',views.eliminarProducto,name='eliminarProducto')
    
]