from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from empleados.models import Empleado, Cargo

@login_required
def home(request):
    total_empleados = Empleado.objects.count()
    total_cargos = Cargo.objects.count()
    return render(request, 'home/home.html', {
        'total_empleados': total_empleados,
        'total_cargos': total_cargos,
    })