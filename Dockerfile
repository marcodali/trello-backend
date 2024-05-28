# Usar una imagen base oficial de Python 3.9
FROM python:3.9-slim

# Instalar el agente de CloudWatch Logs
RUN apt-get update && apt-get install -y awscli

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requisitos y las dependencias de instalación
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copiar el resto de la aplicación al contenedor
COPY . .

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 80

# Comando para ejecutar la aplicación usando gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "app:app"]
