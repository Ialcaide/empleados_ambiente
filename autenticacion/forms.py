from django import forms
from django.contrib.auth.models import User
import re

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 4:
            raise forms.ValidationError('El usuario debe tener al menos 4 caracteres.')
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise forms.ValidationError('El usuario solo puede contener letras, números y guiones bajos.')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(f'El usuario "{username}" ya está registrado.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('El correo es obligatorio.')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(f'El correo "{email}" ya está registrado.')
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
        if not re.search(r'[A-Z]', password1):
            raise forms.ValidationError('La contraseña debe tener al menos una letra mayúscula.')
        if not re.search(r'[0-9]', password1):
            raise forms.ValidationError('La contraseña debe tener al menos un número.')
        if not re.search(r'[!@#$%^&*()_+\-=\[\]{}|]', password1):
            raise forms.ValidationError('La contraseña debe tener al menos un carácter especial (!@#$%^&*...).')
        return password1

    def clean_password2(self):
        p1 = self.cleaned_data.get('password1')
        p2 = self.cleaned_data.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return p2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user