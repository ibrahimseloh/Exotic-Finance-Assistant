#!/bin/bash

# Démarrer FastAPI en arrière-plan
uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000} &

# Démarrer Streamlit en arrière-plan
streamlit run streamlit_app.py \
    --server.port ${STREAMLIT_PORT:-8501} \
    --server.headless true \
    --server.enableCORS false \
    --server.enableXsrfProtection false &

# Garder le conteneur en vie
tail -f /dev/null
