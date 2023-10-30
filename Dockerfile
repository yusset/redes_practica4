# Usa la imagen base de Python 3
FROM python:3

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el código fuente al contenedor
COPY . /app

# Instala las dependencias (en este caso, solo necesitamos el módulo 'socket')
RUN pip install socket

# Comando de inicio para ejecutar el script Python
CMD ["python", "http_client.py"]
