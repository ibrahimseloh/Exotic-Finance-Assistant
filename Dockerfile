# Utiliser une image de base Python officielle
FROM python:3.10-slim

# Définir les variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000 \
    STREAMLIT_PORT=8501

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    libpoppler-cpp-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Créer et définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
COPY . .

# Installer les dépendances Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Exposer les ports
EXPOSE $PORT
EXPOSE $STREAMLIT_PORT

# Script de démarrage pour lancer les deux services
CMD ["sh", "-c", \
    "uvicorn main:app --host 0.0.0.0 --port $PORT & \
     streamlit run streamlit_app.py --server.port $STREAMLIT_PORT --server.headless true --server.enableCORS false --server.enableXsrfProtection false"]
