from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("ventas/", views.ventas, name="ventas"),
    path("ventas/buscar/", views.buscar_venta, name="buscar_ventas"),
    path("ventas/alta/", views.alta_venta, name="alta_venta"),
    path("ventas/<int:venta_id>/", views.editar_venta, name="editar_venta"),
    path("ventas/<int:venta_id>/complete/", views.complete_ventas, name="complete_ventas"),
    path("ventas/<int:venta_id>/delete/", views.baja_venta, name="delete_ventas"),
    path("logout/", views.logout_view, name="logout"),
    path("login/", views.login_view, name="login"),
    path("clientes/", views.clientes, name="clientes"),
    path("clientes/create/", views.create_cliente, name="create_cliente"),
    path("clientes/<int:cliente_id>/", views.cliente_detail, name="cliente_detail"),
    path("clientes/<int:cliente_id>/complete/", views.complete_cliente, name="complete_cliente"),
    path("clientes/<int:cliente_id>/delete/", views.delete_cliente, name="delete_cliente"),
    path("clientes/completed/", views.clientes_completed, name="clientes_completed"),
]
 