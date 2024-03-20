FROM python:3.10

# Instala las dependencias
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copia el script Python al contenedor
COPY PythonDocker.py .

# Instala las dependencias de Python
RUN pip install webbrowser

# Ejecuta tu script Python cuando se inicie el contenedor
CMD ["python", "PythonDocker.py"]
