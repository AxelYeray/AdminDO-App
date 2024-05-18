from django import forms
from .models import Venta


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ["nombre", "descripcion", "importante", "total", "id"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Cliente nombre"}
            ),
            "descripcion": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Descripción"}
            ),
            "importante": forms.CheckboxInput(
                attrs={"class": "form-check-input md-auto"}
            ),
            "total": forms.NumberInput(attrs={"class": "form-control"}),
        }
