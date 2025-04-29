# Usar imagen base ligera de Python
FROM python:3.11.5-slim-bullseye

# Actualizar e instalar Chromium y librerías necesarias
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
    && apt-get clean

# Copiar archivos del proyecto
COPY requirements.txt .
COPY graficos.py .
COPY scraping.py .
COPY volatilidad.py .
COPY streamlit_app.py .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para arrancar Streamlit
ENTRYPOINT [ "streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0" ]



