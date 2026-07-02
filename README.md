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
- Listar, registrar, editar y eliminar **Empleados** y **Cargos**
- Ver detalle completo de empleados y cargos
- Activar o desactivar empleados
- Filtrar empleados por nombre, cargo, fecha, sueldo y estado
- Exportar listas a **Excel** y **PDF**
- Paginación en todas las listas
- Autenticación con login, register y logout
- Rutas protegidas (solo accesibles con sesión iniciada)
- Dashboard Home con estadísticas en tiempo real
- Mensajes de confirmación tipo toast

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Descripción |
|------------|-------------|
| Python 3.14 | Lenguaje de programación |
| Django 6.0.6 | Framework web backend |
| Bootstrap 5.3 | Framework CSS para la interfaz |
| Bootstrap Icons | Iconografía moderna |
| Chart.js | Gráfica de empleados por cargo |
| openpyxl | Exportación a Excel |
| ReportLab | Exportación a PDF |
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
│   ├── static/empleados/css/styles.css
│   ├── templates/empleados/
│   │   ├── base.html
│   │   ├── empleado_lista.html
│   │   ├── empleado_form.html
│   │   ├── empleado_detalle.html
│   │   ├── empleado_confirmar_eliminar.html
│   │   ├── cargo_lista.html
│   │   ├── cargo_form.html
│   │   ├── cargo_detalle.html
│   │   └── cargo_confirmar_eliminar.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── empleados_vbc/          # App secundaria - CRUD con VBC
│   ├── static/empleados_vbc/css/styles.css
│   ├── templates/empleados_vbc/
│   │   ├── base.html
│   │   ├── empleado_lista.html
│   │   ├── empleado_form.html
│   │   ├── empleado_detalle.html
│   │   ├── cargo_lista.html
│   │   ├── cargo_form.html
│   │   └── cargo_detalle.html
│   ├── views.py
│   └── urls.py
├── autenticacion/          # App de autenticación
│   ├── static/autenticacion/css/styles.css
│   ├── templates/autenticacion/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── perfil.html
│   │   └── cambiar_password.html
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── home/                   # App del dashboard principal
│   ├── static/home/css/styles.css
│   ├── templates/home/home.html
│   ├── views.py
│   └── urls.py
├── .env
├── .gitignore
├── build.sh
├── Procfile
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
| activo | BooleanField (default: True) |

---

## ✅ Validaciones implementadas

### Empleado
- Nombres y apellidos: solo letras, mínimo 2 caracteres, obligatorio dos nombres y dos apellidos
- Correo: único por empleado
- Sueldo: no negativo, no menor a $482 (salario básico), no mayor a $7,000
- Fecha de ingreso: no futura, no mayor a 50 años atrás

### Cargo
- Nombre: solo letras, no puede repetirse
- Descripción: mínimo 10 caracteres si se ingresa

### Registro de usuario
- Usuario: mínimo 4 caracteres, solo letras/números/guión bajo, único
- Email: obligatorio, único
- Contraseña: mínimo 8 caracteres, una mayúscula, un número, un carácter especial

---

## 🔗 URLs disponibles

| URL | Descripción |
|-----|-------------|
| `/` | Redirige al Home |
| `/home/` | Dashboard principal |
| `/login/` | Iniciar sesión |
| `/register/` | Registrar cuenta |
| `/logout/` | Cerrar sesión |
| `/perfil/` | Perfil del usuario |
| `/empleados/` | Lista de empleados (VBF) |
| `/empleados/nuevo/` | Nuevo empleado (VBF) |
| `/empleados/detalle/<pk>/` | Detalle de empleado (VBF) |
| `/empleados/exportar/excel/` | Exportar empleados a Excel (VBF) |
| `/empleados/exportar/pdf/` | Exportar empleados a PDF (VBF) |
| `/cargos/` | Lista de cargos (VBF) |
| `/cargos/nuevo/` | Nuevo cargo (VBF) |
| `/cargos/detalle/<pk>/` | Detalle de cargo (VBF) |
| `/cargos/exportar/excel/` | Exportar cargos a Excel (VBF) |
| `/cargos/exportar/pdf/` | Exportar cargos a PDF (VBF) |
| `/vbc/empleados/` | Lista de empleados (VBC) |
| `/vbc/empleados/detalle/<pk>/` | Detalle de empleado (VBC) |
| `/vbc/empleados/exportar/excel/` | Exportar empleados a Excel (VBC) |
| `/vbc/empleados/exportar/pdf/` | Exportar empleados a PDF (VBC) |
| `/vbc/cargos/` | Lista de cargos (VBC) |
| `/vbc/cargos/detalle/<pk>/` | Detalle de cargo (VBC) |
| `/vbc/cargos/exportar/excel/` | Exportar cargos a Excel (VBC) |
| `/vbc/cargos/exportar/pdf/` | Exportar cargos a PDF (VBC) |

---

## 🔄 Comparación VBF vs VBC

| Característica | VBF | VBC |
|---------------|-----|-----|
| Decorador de protección | `@login_required` | `LoginRequiredMixin` |
| Definición de vista | Función `def` | Clase con herencia |
| Exportar Excel/PDF | Función `def` | Clase `View` con método `get` |
| Detalle de registro | Función `def` | Clase `DetailView` |
| Paginación | Manual con `Paginator` | Automática con `paginate_by` |
| Código requerido | Más explícito | Más conciso |
| Flexibilidad | Alta | Media-Alta |
| Curva de aprendizaje | Baja | Media |

---

## 🏠 Dashboard Home

El panel principal muestra:
- Total de empleados registrados
- Total de cargos registrados
- Empleados activos
- Empleados inactivos
- Gráfica de barras — empleados por cargo
- Acciones rápidas
- Selector para entrar a VBF o VBC

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