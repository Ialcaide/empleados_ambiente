from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from empleados.models import Cargo, Empleado
from empleados.forms import CargoForm, EmpleadoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

class EmpleadoDetailView(LoginRequiredMixin, DetailView):
    model = Empleado
    template_name = 'empleados_vbc/empleado_detalle.html'
    context_object_name = 'empleado'

class CargoDetailView(LoginRequiredMixin, DetailView):
    model = Cargo
    template_name = 'empleados_vbc/cargo_detalle.html'
    context_object_name = 'cargo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empleados'] = Empleado.objects.filter(cargo=self.object)
        return context

# ─── CARGOS ───────────────────────────────────────────

class CargoListView(LoginRequiredMixin, ListView):
    model = Cargo
    template_name = 'empleados_vbc/cargo_lista.html'
    context_object_name = 'cargos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '')
        if query:
            queryset = queryset.filter(nombre__icontains=query) | queryset.filter(descripcion__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

class CargoCreateView(LoginRequiredMixin, CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'empleados_vbc/cargo_form.html'
    success_url = reverse_lazy('vbc_cargo_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo Cargo (VBC)'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Cargo creado exitosamente.')
        return super().form_valid(form)

class CargoUpdateView(LoginRequiredMixin, UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'empleados_vbc/cargo_form.html'
    success_url = reverse_lazy('vbc_cargo_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cargo (VBC)'
        return context

    def form_valid(self, form):
        messages.success(self.request, f'Cargo "{self.object.nombre}" actualizado exitosamente.')
        return super().form_valid(form)

class CargoDeleteView(LoginRequiredMixin, DeleteView):
    model = Cargo
    template_name = 'empleados_vbc/cargo_confirmar_eliminar.html'
    success_url = reverse_lazy('vbc_cargo_lista')
    context_object_name = 'objeto'

    def form_valid(self, form):
        messages.success(self.request, f'Cargo "{self.object.nombre}" eliminado exitosamente.')
        return super().form_valid(form)

# ─── EMPLEADOS ────────────────────────────────────────

class EmpleadoListView(LoginRequiredMixin, ListView):
    model = Empleado
    template_name = 'empleados_vbc/empleado_lista.html'
    context_object_name = 'empleados'
    paginate_by = 10

    def get_queryset(self):
        queryset = Empleado.objects.select_related('cargo').all()
        query = self.request.GET.get('q', '')
        cargo_filtro = self.request.GET.get('cargo', '')
        fecha_desde = self.request.GET.get('fecha_desde', '')
        fecha_hasta = self.request.GET.get('fecha_hasta', '')
        sueldo_min = self.request.GET.get('sueldo_min', '')
        sueldo_max = self.request.GET.get('sueldo_max', '')
        if query:
            queryset = queryset.filter(nombres__icontains=query) | queryset.filter(apellidos__icontains=query)
        if cargo_filtro:
            queryset = queryset.filter(cargo__id=cargo_filtro)
        if fecha_desde:
            queryset = queryset.filter(fecha_ingreso__gte=fecha_desde)
        if fecha_hasta:
            queryset = queryset.filter(fecha_ingreso__lte=fecha_hasta)
        if sueldo_min:
            queryset = queryset.filter(sueldo__gte=sueldo_min)
        if sueldo_max:
            queryset = queryset.filter(sueldo__lte=sueldo_max)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['cargo_filtro'] = self.request.GET.get('cargo', '')
        context['fecha_desde'] = self.request.GET.get('fecha_desde', '')
        context['fecha_hasta'] = self.request.GET.get('fecha_hasta', '')
        context['sueldo_min'] = self.request.GET.get('sueldo_min', '')
        context['sueldo_max'] = self.request.GET.get('sueldo_max', '')
        context['cargos'] = Cargo.objects.all()
        return context

class EmpleadoCreateView(LoginRequiredMixin, CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados_vbc/empleado_form.html'
    success_url = reverse_lazy('vbc_empleado_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo Empleado (VBC)'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Empleado creado exitosamente.')
        return super().form_valid(form)

class EmpleadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados_vbc/empleado_form.html'
    success_url = reverse_lazy('vbc_empleado_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Empleado (VBC)'
        return context

    def form_valid(self, form):
        messages.success(self.request, f'Empleado "{self.object.nombres}" actualizado exitosamente.')
        return super().form_valid(form)

class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Empleado
    template_name = 'empleados_vbc/empleado_confirmar_eliminar.html'
    success_url = reverse_lazy('vbc_empleado_lista')
    context_object_name = 'objeto'

    def form_valid(self, form):
        messages.success(self.request, f'Empleado "{self.object.nombres}" eliminado exitosamente.')
        return super().form_valid(form)