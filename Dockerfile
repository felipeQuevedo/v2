FROM python:3.9-slim

# Instala las dependencias
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Crea un directorio para la aplicación
RUN mkdir /app

# Copia el script Python al directorio de la aplicación
COPY PythonDocker.py /app/


# Establece el directorio de trabajo
WORKDIR /app

# Ejecuta tu script Python cuando se inicie el contenedor
CMD ["python", "PythonDocker.py"]
