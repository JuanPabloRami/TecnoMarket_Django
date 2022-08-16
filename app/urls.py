from django.urls import path, include
from . import views
from rest_framework import routers

router =routers.DefaultRouter()
router.register('producto',views.ProductoViewSet)
router.register('marca',views.MarcaViewSet)


urlpatterns = [
    path('',views.index,name='home'),
    path('contacto/',views.contacto,name='contacto'),
    path('galeria/',views.galeria,name='galeria'), 
    path('agregar-producto/',views.agregarProducto,name='agregarProducto'),
    path('listar-producto/',views.listarProducto,name='listarProducto'),
    path('modificar-producto/<id>/',views.modificarProducto,name='modificarProducto'),
    path('eliminar-producto/<id>/',views.eliminarProducto,name='eliminarProducto'),
    path('registro/',views.registro, name='registro'),
    path('error-facebook/',views.errorFacebook,name='errorFacebook'),
    path('api/',include(router.urls)),
    
]