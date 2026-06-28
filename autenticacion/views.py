from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cuenta creada exitosamente. Inicia sesión.')
        return redirect('login')
    return render(request, 'autenticacion/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('empleado_lista')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'autenticacion/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')