# 🔐 Password Generator (Python)

Generador de contraseñas seguro desarrollado en **Python** con **interfaz gráfica en Tkinter**.
El proyecto está diseñado con una **arquitectura modular**, separando la interfaz, la lógica de generación, los servicios y el almacenamiento.

El objetivo del proyecto es evolucionar desde un simple generador hacia una **herramienta profesional de generación y análisis de contraseñas**, incorporando prácticas reales de desarrollo como separación de responsabilidades, seguridad criptográfica y extensibilidad.

---

# ✨ Características actuales

### 🔑 Generación segura de contraseñas

* Generación criptográficamente segura usando `secrets`
* Configuración de longitud de contraseña
* Selección de tipos de caracteres:

  * 🔡 Letras minúsculas
  * 🔠 Letras mayúsculas
  * 🔢 Números
  * 🔣 Símbolos especiales

### 🖥️ Interfaz gráfica

Interfaz simple desarrollada con **Tkinter** que permite:

* Configurar parámetros de generación
* Generar contraseñas con un solo clic
* Visualizar la contraseña generada

### 💾 Persistencia

* Guardado opcional de contraseñas generadas
* Registro automático con **fecha y hora**
* Almacenamiento en:

```
data/passwords.txt
```
### 🔐 Análisis de seguridad

* Cálculo de entropía criptográfica
* Indicador de fortaleza de contraseña

  * Débil
  * Media
  * Fuerte
  * Muy fuerte

### 📋 Usabilidad

* Copiar contraseña al portapapeles con un clic
* Notificación cuando la contraseña ha sido copiada

---

# 🏗️ Arquitectura del proyecto

El proyecto sigue una estructura modular que separa responsabilidades.

```
password_generator/
│
├── core/
│   └── generator.py           # Lógica criptográfica de generación     
│
├── utils/
│   └── clipboard.py           # Gestión del portapapeles
│
├── services/
│   └── password_service.py    # Lógica de negocio para crear contraseñas
│
├── storage/
│   └── file_storage.py        # Gestión del almacenamiento en archivos
│
├── security/
│   └── entropy.py             # Lógica patra calcular la entropia de la contraseña
│
├── ui/
│   └── gui.py                 # Interfaz gráfica con Tkinter
│
├── data/
│   └── passwords.txt
│
├── venv/ # Entorno virtual 
├── main.py                    # Punto de entrada de la aplicación
│
└── README.md
```

### Separación de responsabilidades

| Módulo   | Responsabilidad                         |
| -------- | --------------------------------------- |
| core     | generación criptográfica de contraseñas |
| services | reglas de negocio                       |
| storage  | persistencia de datos                   |
| security | entropía de contraseña                  |
| ui       | interfaz gráfica                        |
| main     | inicialización de la aplicación         |

Esta arquitectura facilita:

* mantenimiento
* escalabilidad
* pruebas unitarias
* futuras extensiones del sistema

---

# ⚙️ Requisitos

* Python **3.10+**
* Tkinter (incluido en la mayoría de instalaciones de Python)

---

# 📦 Instalación

Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/password-generator.git
```

Entra al proyecto:

```bash
cd password-generator
```

Crear entorno virtual (recomendado):

```bash
python -m venv venv
```

Activar entorno virtual:

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

---

# ▶️ Ejecutar la aplicación

```bash
python main.py
```

Se abrirá la interfaz gráfica del generador de contraseñas.

---

# 🧪 Ejemplo de contraseña generada

```
nT8@Pq2!kLm3
```

---

# 🛣️ Roadmap (mejoras futuras)

El proyecto continuará evolucionando hacia una herramienta más completa.

### Seguridad

* [x] Cálculo de **entropía de contraseña**
* [x] Indicador de seguridad (débil / media / fuerte)
* [ ] Validación contra contraseñas débiles
* [ ] Generación tipo **passphrase (Diceware)**

### Funcionalidades

* [x] Botón **copiar al portapapeles**
* [ ] Historial de contraseñas generadas
* [ ] Guardado por **servicio (gmail, github, etc.)**
* [ ] Exportación segura

### Seguridad avanzada

* [ ] Cifrado de almacenamiento con **AES**
* [ ] Protección con contraseña maestra
* [ ] Gestión básica de contraseñas

### Desarrollo

* [ ] Pruebas unitarias con **pytest**
* [ ] Empaquetado como **paquete Python**
* [ ] Versión CLI (terminal)
* [ ] Generación de ejecutable con **PyInstaller**

### Versión futura

* [ ] API REST
* [ ] Aplicación web (Django / FastAPI)
* [ ] Dashboard de análisis de contraseñas

---

# 🎯 Objetivo del proyecto

Este proyecto forma parte de un proceso de aprendizaje enfocado en:

* desarrollo backend con Python
* diseño de software modular
* seguridad informática aplicada
* construcción de herramientas reales

---

# 🤝 Contribuciones

Las contribuciones, sugerencias y mejoras son bienvenidas.

Puedes:

* abrir un **issue**
* proponer una mejora
* enviar un **pull request**

---

# 📄 Licencia

Este proyecto está disponible bajo la licencia **MIT**.
