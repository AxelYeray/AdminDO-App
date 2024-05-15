from django.contrib import admin
from .models import Venta, Cliente


class VentaAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)


# Register your models here.
admin.site.register(Venta, VentaAdmin)
admin.site.register(Cliente)
