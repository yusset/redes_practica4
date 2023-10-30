# Utiliza una imagen base de Windows Server Core
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Establece el directorio de trabajo
WORKDIR C:\app

# Copia el código fuente de la aplicación al contenedor
COPY clienteHTTP.py .

# Instala Python
ADD https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64-webinstall.msi C:\python_installer.msi
RUN powershell -Command Start-Process -Wait -FilePath msiexec -ArgumentList '/i', 'C:\python_installer.msi', '/qn'
RUN del C:\python_installer.msi

# Comando de inicio para ejecutar la aplicación
CMD ["python", "clienteHTTP.py"]
