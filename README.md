## 🚀 Requisitos

Antes de comenzar, asegúrate de tener lo siguiente instalado:

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## ⚙️ Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/soandrade6/appterio-api.git
   cd appterio-api

2. **Crear un entorno virtual**:
   ```bash
   python -m venv venv


3. **Activar el entorno virtual**:
   ```bash
   venv\Scripts\activate #Windows
   source venv/bin/activate #Linux/MacOS


4. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt

## ⚙️ Ejecución del proyecto

2. **Ejecutar el servidor**:   
    ```bash
    uvicorn app.main:app --reload

Esto arrancará el servidor de FastAPI en el puerto 8000 (por defecto). Puedes acceder a la API desde tu navegador en http://127.0.0.1:8000.