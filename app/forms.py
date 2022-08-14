from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxFileSizeValidator
from django.forms import ValidationError

class ContactoForm(forms.ModelForm):

    class Meta:
        model=Contacto
        # fields=['nombre','correo','tipoconsulta','mensaje','avisos']
        fields='__all__'

class ProductoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3,max_length=23)
    imagen = forms.ImageField(required=False, validators=[MaxFileSizeValidator(max_file_Size = 1)])
    precio = forms.IntegerField(min_value=1,max_value=100000000)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexact = nombre).exists()

        if existe:
            raise ValidationError(f"el nombre '{nombre}' ya esta en uso, ingresa otro nombre.")
        
        return nombre


    class Meta:
        model=Producto
        fields='__all__'
        widgets={
            "fecha_fabricacion":forms.SelectDateWidget()
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields= ["username","first_name","last_name","email","password1","password2"]


    