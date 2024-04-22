from django.forms import ModelForm
from .models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "apellido", "calle", "colonia", "celular", "folio","important"]
