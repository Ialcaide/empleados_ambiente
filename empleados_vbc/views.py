from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from empleados.models import Cargo, Empleado
from empleados.forms import CargoForm, EmpleadoForm

# ─── CARGOS ───────────────────────────────────────────

class CargoListView(ListView):
    model = Cargo
    template_name = 'empleados_vbc/cargo_lista.html'
    context_object_name = 'cargos'

class CargoCreateView(CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'empleados_vbc/cargo_form.html'
    success_url = reverse_lazy('vbc_cargo_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo Cargo (VBC)'
        return context

class CargoUpdateView(UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'empleados_vbc/cargo_form.html'
    success_url = reverse_lazy('vbc_cargo_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cargo (VBC)'
        return context

class CargoDeleteView(DeleteView):
    model = Cargo
    template_name = 'empleados_vbc/cargo_confirmar_eliminar.html'
    success_url = reverse_lazy('vbc_cargo_lista')
    context_object_name = 'objeto'

# ─── EMPLEADOS ────────────────────────────────────────

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleados_vbc/empleado_lista.html'
    context_object_name = 'empleados'

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados_vbc/empleado_form.html'
    success_url = reverse_lazy('vbc_empleado_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo Empleado (VBC)'
        return context

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados_vbc/empleado_form.html'
    success_url = reverse_lazy('vbc_empleado_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Empleado (VBC)'
        return context

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleados_vbc/empleado_confirmar_eliminar.html'
    success_url = reverse_lazy('vbc_empleado_lista')
    context_object_name = 'objeto'