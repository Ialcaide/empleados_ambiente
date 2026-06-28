from django.shortcuts import render, get_object_or_404, redirect
from .models import Cargo, Empleado
from .forms import CargoForm, EmpleadoForm

# ─── CARGOS ───────────────────────────────────────────

def cargo_lista(request):
    cargos = Cargo.objects.all()
    return render(request, 'empleados/cargo_lista.html', {'cargos': cargos})

def cargo_crear(request):
    form = CargoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cargo_lista')
    return render(request, 'empleados/cargo_form.html', {'form': form, 'titulo': 'Nuevo Cargo'})

def cargo_editar(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    form = CargoForm(request.POST or None, instance=cargo)
    if form.is_valid():
        form.save()
        return redirect('cargo_lista')
    return render(request, 'empleados/cargo_form.html', {'form': form, 'titulo': 'Editar Cargo'})

def cargo_eliminar(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    if request.method == 'POST':
        cargo.delete()
        return redirect('cargo_lista')
    return render(request, 'empleados/cargo_confirmar_eliminar.html', {'objeto': cargo, 'tipo': 'cargo'})

# ─── EMPLEADOS ────────────────────────────────────────

def empleado_lista(request):
    empleados = Empleado.objects.select_related('cargo').all()
    return render(request, 'empleados/empleado_lista.html', {'empleados': empleados})

def empleado_crear(request):
    form = EmpleadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('empleado_lista')
    return render(request, 'empleados/empleado_form.html', {'form': form, 'titulo': 'Nuevo Empleado'})

def empleado_editar(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    form = EmpleadoForm(request.POST or None, instance=empleado)
    if form.is_valid():
        form.save()
        return redirect('empleado_lista')
    return render(request, 'empleados/empleado_form.html', {'form': form, 'titulo': 'Editar Empleado'})

def empleado_eliminar(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleado_lista')
    return render(request, 'empleados/empleado_confirmar_eliminar.html', {'objeto': empleado, 'tipo': 'empleado'})