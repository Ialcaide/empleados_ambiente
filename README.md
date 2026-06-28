# 📋 CRUD Empleados y Cargos — Django

Proyecto universitario desarrollado para la asignatura de **Desarrollo Web con Python/Django** en la Universidad Estatal de Milagro (UNEMI). Implementa un sistema CRUD completo para la gestión de Empleados y Cargos, con autenticación de usuarios y despliegue en producción.

---

## 🚀 Demo en vivo

🔗 [https://empleados-ambiente.onrender.com](https://empleados-ambiente.onrender.com)

---

## 📌 Descripción

Este proyecto demuestra la implementación de un CRUD utilizando dos enfoques de Django:

- **VBF** — Vistas Basadas en Funciones (`/empleados/`, `/cargos/`)
- **VBC** — Vistas Basadas en Clases (`/vbc/empleados/`, `/vbc/cargos/`)

Ambas implementaciones permiten:
- Listar, registrar, editar y eliminar **Empleados**
- Listar, registrar, editar y eliminar **Cargos**
- Autenticación con login, register y logout
- Rutas protegidas (solo accesibles con sesión iniciada)

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Descripción |
|------------|-------------|
| Python 3.14 | Lenguaje de programación |
| Django 6.0.6 | Framework web backend |
| Bootstrap 5.3 | Framework CSS para la interfaz |
| SQLite | Base de datos local |
| PostgreSQL | Base de datos en producción (Render) |
| Gunicorn | Servidor WSGI para producción |
| WhiteNoise | Manejo de archivos estáticos |
| Render.com | Plataforma de despliegue gratuito |

---

## 📁 Estructura del proyecto

```
crud_empleados/
├── core/                   # Configuración principal del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── empleados/              # App principal - CRUD con VBF
│   ├── migrations/
│   ├── templates/
│   │   └── empleados/
│   │       ├── base.html
│   │       ├── empleado_lista.html
│   │       ├── empleado_form.html
│   │       ├── empleado_confirmar_eliminar.html
│   │       ├── cargo_lista.html
│   │       ├── cargo_form.html
│   │       └── cargo_confirmar_eliminar.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── empleados_vbc/          # App secundaria - CRUD con VBC
│   ├── templates/
│   │   └── empleados_vbc/
│   ├── views.py
│   └── urls.py
├── autenticacion/          # App de autenticación
│   ├── templates/
│   │   └── autenticacion/
│   │       ├── login.html
│   │       └── register.html
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── .env                    # Variables de entorno (no subir a GitHub)
├── .gitignore
├── build.sh                # Script de build para Render
├── Procfile                # Configuración de servidor para Render
├── manage.py
└── requirements.txt
```

---

## 🗄️ Modelos

### Cargo
| Campo | Tipo |
|-------|------|
| nombre | CharField (máx. 100) |
| descripcion | CharField (máx. 200, opcional) |

### Empleado
| Campo | Tipo |
|-------|------|
| nombres | CharField (máx. 100) |
| apellidos | CharField (máx. 100) |
| correo | EmailField |
| sueldo | DecimalField (10 dígitos, 2 decimales) |
| fecha_ingreso | DateField |
| cargo | ForeignKey → Cargo |

---

## ⚙️ Instalación local

### 1. Clonar el repositorio
```bash
git clone https://github.com/Ialcaide/empleados_ambiente.git
cd empleados_ambiente
```

### 2. Crear y activar el entorno virtual
```bash
python -m venv ambiente
# Windows:
ambiente\Scripts\Activate.ps1
# Linux/Mac:
source ambiente/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Crear archivo `.env`
```
SECRET_KEY=tu_clave_secreta
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Aplicar migraciones
```bash
python manage.py migrate
```

### 6. Crear superusuario
```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor
```bash
python manage.py runserver
```

Abre el navegador en `http://127.0.0.1:8000/`

---

## 🔗 URLs disponibles

| URL | Descripción |
|-----|-------------|
| `/` | Redirige a la lista de empleados |
| `/login/` | Iniciar sesión |
| `/register/` | Registrar cuenta |
| `/logout/` | Cerrar sesión |
| `/empleados/` | Lista de empleados (VBF) |
| `/empleados/nuevo/` | Nuevo empleado (VBF) |
| `/cargos/` | Lista de cargos (VBF) |
| `/cargos/nuevo/` | Nuevo cargo (VBF) |
| `/vbc/empleados/` | Lista de empleados (VBC) |
| `/vbc/cargos/` | Lista de cargos (VBC) |

---

## 🔄 Comparación VBF vs VBC

| Característica | VBF | VBC |
|---------------|-----|-----|
| Decorador de protección | `@login_required` | `LoginRequiredMixin` |
| Definición de vista | Función `def` | Clase con herencia |
| Código requerido | Más explícito | Más conciso |
| Flexibilidad | Alta | Media-Alta |
| Curva de aprendizaje | Baja | Media |

---

## 🌐 Despliegue en Render.com

El proyecto está configurado para desplegarse automáticamente en Render:

- **Build Command:** `./build.sh`
- **Start Command:** `gunicorn core.wsgi:application`
- **Variables de entorno:** `SECRET_KEY`, `DEBUG`, `DATABASE_URL`

Cada `git push` a la rama `main` activa un nuevo deploy automático.

---

## 👩‍💻 Autora

**Ileana Alcaide**
Estudiante de Ingeniería en Software — 4to semestre
Universidad Estatal de Milagro (UNEMI)
Período Abril — Agosto 2026
