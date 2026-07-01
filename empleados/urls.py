from django.urls import path
from . import views

urlpatterns = [
    # Cargos
    path('cargos/', views.cargo_lista, name='cargo_lista'),
    path('cargos/nuevo/', views.cargo_crear, name='cargo_crear'),
    path('cargos/editar/<int:pk>/', views.cargo_editar, name='cargo_editar'),
    path('cargos/eliminar/<int:pk>/', views.cargo_eliminar, name='cargo_eliminar'),

    # Empleados
    path('empleados/', views.empleado_lista, name='empleado_lista'),
    path('empleados/nuevo/', views.empleado_crear, name='empleado_crear'),
    path('empleados/editar/<int:pk>/', views.empleado_editar, name='empleado_editar'),
    path('empleados/eliminar/<int:pk>/', views.empleado_eliminar, name='empleado_eliminar'),
    path('home/', views.home, name='home'),
]