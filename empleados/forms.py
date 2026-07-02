from django import forms
from .models import Cargo, Empleado
from datetime import date
import re

SALARIO_BASICO = 482

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            raise forms.ValidationError('El nombre del cargo solo puede contener letras y espacios.')
        qs = Cargo.objects.filter(nombre__iexact=nombre)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(f'Ya existe un cargo con el nombre "{nombre}".')
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if descripcion and len(descripcion) < 10:
            raise forms.ValidationError('La descripción debe tener al menos 10 caracteres.')
        return descripcion


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombres', 'apellidos', 'correo', 'sueldo', 'fecha_ingreso', 'cargo', 'activo']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'sueldo': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'cargo': forms.Select(attrs={'class': 'form-select'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk and self.instance.fecha_ingreso:
            self.initial['fecha_ingreso'] = self.instance.fecha_ingreso.strftime('%Y-%m-%d')

    def clean_nombres(self):
        nombres = self.cleaned_data.get('nombres')
        if len(nombres) < 2:
            raise forms.ValidationError('El nombre debe tener al menos 2 caracteres.')
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombres):
            raise forms.ValidationError('El nombre solo puede contener letras y espacios.')
        return nombres

    def clean_apellidos(self):
        apellidos = self.cleaned_data.get('apellidos')
        if len(apellidos) < 2:
            raise forms.ValidationError('Los apellidos deben tener al menos 2 caracteres.')
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', apellidos):
            raise forms.ValidationError('Los apellidos solo pueden contener letras y espacios.')
        partes = apellidos.strip().split()
        if len(partes) < 2:
            raise forms.ValidationError('Debes ingresar los dos apellidos.')
        return apellidos

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        qs = Empleado.objects.filter(correo__iexact=correo)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(f'Ya existe un empleado registrado con el correo "{correo}".')
        return correo

    def clean_sueldo(self):
        sueldo = self.cleaned_data.get('sueldo')
        if sueldo is not None:
            if sueldo < 0:
                raise forms.ValidationError(f'El sueldo no puede ser negativo. Ingresaste: ${sueldo}.')
            if sueldo < SALARIO_BASICO:
                raise forms.ValidationError(f'El sueldo (${sueldo}) no puede ser menor al salario básico de ${SALARIO_BASICO}.')
            if sueldo > 7000:
                raise forms.ValidationError(f'El sueldo (${sueldo}) no puede ser mayor a $7,000.')
        return sueldo

    def clean_fecha_ingreso(self):
        fecha = self.cleaned_data.get('fecha_ingreso')
        if fecha is not None:
            hoy = date.today()
            años_diferencia = (hoy - fecha).days / 365
            if años_diferencia > 50:
                raise forms.ValidationError(f'La fecha de ingreso no puede ser mayor a 50 años atrás. Ingresaste: {fecha}.')
            if fecha > hoy:
                raise forms.ValidationError('La fecha de ingreso no puede ser una fecha futura.')
        return fecha

    def clean_cargo(self):
        cargo = self.cleaned_data.get('cargo')
        if not Cargo.objects.exists():
            raise forms.ValidationError('No hay cargos registrados. Primero debes crear un cargo.')
        return cargo