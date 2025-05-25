import os
import uuid
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.db             import initialize_chroma_db
from src.rag_pipeline   import generate_answer as rag_generate_answer

# --- Configuration via env ---
DB_PATH         = os.getenv("DB_PATH", "chroma_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "exotic_option")
PDF_PATH        = os.getenv("PDF_PATH", "data/exotic_option.pdf")

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

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    request_id: str
    bot_response: str

@app.on_event("startup")
def startup_event():
    global client, collection
    client, collection = initialize_chroma_db(DB_PATH, COLLECTION_NAME)



@app.get("/query", response_model=QueryResponse, summary="Q/A Step")
def query_endpoint(
    query: str = Query(..., description="La question que vous souhaitez poser à l'assistant"),
):
    request_id = str(uuid.uuid4())
    try:
        bot_resp = rag_generate_answer(query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return QueryResponse(request_id=request_id, bot_response=bot_resp)


def cli(query: str):
    response = rag_generate_answer(query)
    print(response)


