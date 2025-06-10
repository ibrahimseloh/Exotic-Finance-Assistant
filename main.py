import os
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.db import initialize_chroma_db
from src.rag_pipeline import generate_answer as rag_generate_answer
from typing import List
from uuid import uuid4
import google.generativeai as genai


# --- Configuration via env ---
DB_PATH = os.getenv("DB_PATH", "chroma_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "Exotic_Option")
PDF_PATH = os.getenv("PDF_PATH", "data/exotic_option.pdf")

# --- FastAPI app ---
app = FastAPI(
    title="Praxis, Exotic Finance Assistant API",
    version="1.0.0",
    description="Intelligent assistant for exotic finance options",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Stockage en mémoire de la clé API
gemini_api_key = None

class QueryResponse(BaseModel):
    request_id: str
    bot_response: str
    sources: List[dict]

@app.on_event("startup")
def startup_event():
    global client, collection
    client, collection = initialize_chroma_db(DB_PATH, COLLECTION_NAME)

@app.get("/set_gemini_key/", summary="Définir la clé API Gemini")
def set_gemini_key(api_key: str = Query(..., description="Votre clé API Gemini")):
    global gemini_api_key
    gemini_api_key = api_key
    genai.configure(api_key=gemini_api_key)
    return {"message": "Clé API Gemini configurée avec succès."}



@app.get("/query", response_model=QueryResponse, summary="Q/A Step")
def query_endpoint(
    query: str = Query(..., description="La question que vous souhaitez poser à l'assistant"),
):
    request_id = str(uuid4())
    
    # Vérifie que la clé API est configurée
    if gemini_api_key is None:
        raise HTTPException(
            status_code=400,
            detail="Clé API Gemini non configurée. Veuillez d'abord appeler /set_gemini_key/"
        )
    
    try:
        response, sources = rag_generate_answer(query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return QueryResponse(
        request_id=request_id,
        bot_response=response,
        sources=sources
    )