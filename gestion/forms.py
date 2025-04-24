from django import forms # type: ignore
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['documento', 'nombres', 'apellidos', 'telefono', 'correo']