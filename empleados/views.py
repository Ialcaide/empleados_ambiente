from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cargo, Empleado
from .forms import CargoForm, EmpleadoForm


# ─── CARGOS ───────────────────────────────────────────

@login_required
def cargo_lista(request):
    cargos = Cargo.objects.all()
    query = request.GET.get('q', '')
    if query:
        cargos = cargos.filter(
            models.Q(nombre__icontains=query) |
            models.Q(descripcion__icontains=query)
        )
    return render(request, 'empleados/cargo_lista.html', {
        'cargos': cargos,
        'query': query,
    })

@login_required
def cargo_crear(request):
    form = CargoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cargo_lista')
    return render(request, 'empleados/cargo_form.html', {'form': form, 'titulo': 'Nuevo Cargo'})

@login_required
def cargo_editar(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    form = CargoForm(request.POST or None, instance=cargo)
    if form.is_valid():
        form.save()
        return redirect('cargo_lista')
    return render(request, 'empleados/cargo_form.html', {'form': form, 'titulo': 'Editar Cargo'})

@login_required
def cargo_eliminar(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    if request.method == 'POST':
        cargo.delete()
        return redirect('cargo_lista')
    return render(request, 'empleados/cargo_confirmar_eliminar.html', {'objeto': cargo})

# ─── EMPLEADOS ────────────────────────────────────────

@login_required
def empleado_lista(request):
    empleados = Empleado.objects.select_related('cargo').all()
    
    query = request.GET.get('q', '')
    cargo_filtro = request.GET.get('cargo', '')
    fecha_desde = request.GET.get('fecha_desde', '')
    fecha_hasta = request.GET.get('fecha_hasta', '')
    sueldo_min = request.GET.get('sueldo_min', '')
    sueldo_max = request.GET.get('sueldo_max', '')

    if query:
        empleados = empleados.filter(
            models.Q(nombres__icontains=query) |
            models.Q(apellidos__icontains=query)
        )
    if cargo_filtro:
        empleados = empleados.filter(cargo__id=cargo_filtro)
    if fecha_desde:
        empleados = empleados.filter(fecha_ingreso__gte=fecha_desde)
    if fecha_hasta:
        empleados = empleados.filter(fecha_ingreso__lte=fecha_hasta)
    if sueldo_min:
        empleados = empleados.filter(sueldo__gte=sueldo_min)
    if sueldo_max:
        empleados = empleados.filter(sueldo__lte=sueldo_max)

    cargos = Cargo.objects.all()
    return render(request, 'empleados/empleado_lista.html', {
        'empleados': empleados,
        'cargos': cargos,
        'query': query,
        'cargo_filtro': cargo_filtro,
        'fecha_desde': fecha_desde,
        'fecha_hasta': fecha_hasta,
        'sueldo_min': sueldo_min,
        'sueldo_max': sueldo_max,
    })

@login_required
def empleado_crear(request):
    form = EmpleadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('empleado_lista')
    return render(request, 'empleados/empleado_form.html', {'form': form, 'titulo': 'Nuevo Empleado'})

@login_required
def empleado_editar(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    form = EmpleadoForm(request.POST or None, instance=empleado)
    if form.is_valid():
        form.save()
        return redirect('empleado_lista')
    return render(request, 'empleados/empleado_form.html', {'form': form, 'titulo': 'Editar Empleado'})

@login_required
def empleado_eliminar(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleado_lista')
    return render(request, 'empleados/empleado_confirmar_eliminar.html', {'objeto': empleado})

