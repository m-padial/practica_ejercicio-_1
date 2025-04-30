# Imagen base ligera
FROM python:3.11.5-slim-bullseye

# Actualizar e instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    wget \
    unzip \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    libxss1 \
    libappindicator1 \
    ca-certificates \
    libgfortran5 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Variables de entorno necesarias para Selenium
ENV CHROME_BIN=/usr/bin/chromium
ENV PATH=$PATH:/usr/bin/chromium

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
# Copia toda la carpeta src con todos sus archivos y submódulos
COPY src/ ./src/
 
# Instalar dependencias Python
RUN pip install --no-cache-dir -r src/requirements.txt

# Exponer el puerto por defecto de Dash
EXPOSE 8050

# Comando para ejecutar la app Dash con Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8050", "src.app_dash:server"]





