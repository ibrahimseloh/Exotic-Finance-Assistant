# Étape 1 : Construire l'image avec Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer les ports utilisés par FastAPI et Streamlit
EXPOSE 8000
EXPOSE 8501

# Démarrer FastAPI et Streamlit
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 8000 & streamlit run streamlit_app.py"]
