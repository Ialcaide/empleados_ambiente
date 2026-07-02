from django.urls import path
from . import views

urlpatterns = [
    # Cargos VBC
    path('vbc/cargos/', views.CargoListView.as_view(), name='vbc_cargo_lista'),
    path('vbc/cargos/nuevo/', views.CargoCreateView.as_view(), name='vbc_cargo_crear'),
    path('vbc/cargos/editar/<int:pk>/', views.CargoUpdateView.as_view(), name='vbc_cargo_editar'),
    path('vbc/cargos/eliminar/<int:pk>/', views.CargoDeleteView.as_view(), name='vbc_cargo_eliminar'),
    path('vbc/cargos/detalle/<int:pk>/', views.CargoDetailView.as_view(), name='vbc_cargo_detalle'),
    path('vbc/cargos/exportar/excel/', views.ExportarCargosExcelView.as_view(), name='vbc_exportar_cargos_excel'),
    path('vbc/cargos/exportar/pdf/', views.ExportarCargosPdfView.as_view(), name='vbc_exportar_cargos_pdf'),

    # Empleados VBC
    path('vbc/empleados/', views.EmpleadoListView.as_view(), name='vbc_empleado_lista'),
    path('vbc/empleados/nuevo/', views.EmpleadoCreateView.as_view(), name='vbc_empleado_crear'),
    path('vbc/empleados/editar/<int:pk>/', views.EmpleadoUpdateView.as_view(), name='vbc_empleado_editar'),
    path('vbc/empleados/eliminar/<int:pk>/', views.EmpleadoDeleteView.as_view(), name='vbc_empleado_eliminar'),
    path('vbc/empleados/detalle/<int:pk>/', views.EmpleadoDetailView.as_view(), name='vbc_empleado_detalle'),
    path('vbc/empleados/exportar/excel/', views.ExportarExcelView.as_view(), name='vbc_exportar_excel'),
    path('vbc/empleados/exportar/pdf/', views.ExportarPdfView.as_view(), name='vbc_exportar_pdf'),

]