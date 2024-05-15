from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import VentaForm
from .forms2 import ClienteForm
from .models import Venta, Cliente
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Crear tus vistas aquí.
def hello(request):
    return HttpResponse("Hello World!")

@login_required
def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "GET":
        return render(request, "register.html", {"form": UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                return render(
                    request,
                    "register.html",
                    {"form": UserCreationForm(), "error": "El usuario ya existe"},
                )
        return render(
            request,
            "register.html",
            {"form": UserCreationForm(), "error": "Las contraseñas no coinciden"},
        )

@login_required
def ventas(request):
    ventas = Venta.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, "ventas.html", {"ventas": ventas})

@login_required
def buscar_venta(request):
    ventas = Venta.objects.filter(user=request.user, datecompleted__isnull=False).order_by("-datecompleted")
    return render(request, "ventas.html", {"ventas": ventas})

@login_required
def alta_venta(request):
    if request.method == "GET":
        return render(request, "create_task.html", {"form": VentaForm()})
    else:
        try:
            form = VentaForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect("ventas")
        except ValueError:
            return render(
                request,
                "create_task.html",
                {"form": VentaForm(), "error": "Los datos son inválidos"},
            )

@login_required
def editar_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id, user=request.user)
    if request.method == "GET":
        form = VentaForm(instance=venta)
        return render(request, "task_detail.html", {"venta": venta, "form": form})
    else:
        try:
            form = VentaForm(request.POST, instance=venta)
            form.save()
            return redirect("ventas")
        except ValueError:
            return render(
                request,
                "task_detail.html",
                {"venta": venta, "form": form, "error": "Error actualizando tarea"},
            )

@login_required
def complete_ventas(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id, user=request.user)
    if request.method == "POST":
        venta.datecompleted = timezone.now()
        venta.save()
        return redirect("ventas")

@login_required
def baja_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id, user=request.user)
    if request.method == "POST":
        venta.delete()
        return redirect("ventas")

def logout_view(request):
    logout(request)
    return redirect("login")


def login_view(request):
    if request.method == "GET":
        return render(request, "login.html", {"form": AuthenticationForm()})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "login.html",
                {
                    "form": AuthenticationForm(),
                    "error": "Usuario y/o contraseña incorrectos",
                },
            )
        else:
            login(request, user)
            return redirect("home")

@login_required
def clientes(request):
    clientes = Cliente.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, "clientes.html", {"clientes": clientes})

@login_required
def clientes_completed(request):
    clientes = Cliente.objects.filter(
        user=request.user, datecompleted__isnull=False
    ).order_by("-datecompleted")
    return render(request, "clientes.html", {"clientes": clientes})

@login_required
def create_cliente(request):
    if request.method == "GET":
        return render(request, "create_cliente.html", {"form": ClienteForm()})
    else:
        try:
            form = ClienteForm(request.POST)
            new_cliente = form.save(commit=False)
            new_cliente.user = request.user
            new_cliente.save()
            return redirect("clientes")
        except ValueError:
            return render(
                request,
                "create_cliente.html",
                {"form": ClienteForm(), "error": "Los datos son inválidos"},
            )

@login_required
def cliente_detail(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id, user=request.user)
    if request.method == "GET":
        form = ClienteForm(instance=cliente)
        return render(
            request, "cliente_detail.html", {"cliente": cliente, "form": form}
        )
    else:
        try:
            form = ClienteForm(request.POST, instance=cliente)
            form.save()
            return redirect("clientes")
        except ValueError:
            return render(
                request,
                "cliente_detail.html",
                {
                    "cliente": cliente,
                    "form": form,
                    "error": "Error actualizando cliente",
                },
            )

@login_required
def complete_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id, user=request.user)
    if request.method == "POST":
        cliente.datecompleted = timezone.now()
        cliente.save()
        return redirect("clientes")

@login_required
def delete_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id, user=request.user)
    if request.method == "POST":
        cliente.delete()
        return redirect("clientes")


