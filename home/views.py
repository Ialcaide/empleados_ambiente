from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from empleados.models import Empleado, Cargo
from django.db.models import Count
import json

@login_required
def home(request):
    total_empleados = Empleado.objects.count()
    total_cargos = Cargo.objects.count()
    total_activos = Empleado.objects.filter(activo=True).count()
    total_inactivos = Empleado.objects.filter(activo=False).count()

    datos_cargo = Cargo.objects.annotate(
        total=Count('empleado')
    ).order_by('-total')

    labels = json.dumps([c.nombre for c in datos_cargo])
    data = json.dumps([c.total for c in datos_cargo])

    return render(request, 'home/home.html', {
        'total_empleados': total_empleados,
        'total_cargos': total_cargos,
        'total_activos': total_activos,
        'total_inactivos': total_inactivos,
        'labels': labels,
        'data': data,
    })