FROM python:3.9-slim

# Instala las dependencias
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*
    
RUN mkdir /app

# Copia el script Python al contenedor
COPY PythonDocker.py /app/
COPY holamundo.html /app/

# Establece el directorio de trabajo
WORKDIR /app

# Ejecuta tu script Python cuando se inicie el contenedor
CMD ["python", "PythonDocker.py"]


