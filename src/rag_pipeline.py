from .llm_utils import convert_to_eng, model
from prompt import system_prompt
from src.db import initialize_chroma_db
import tiktoken
import re

client, collection = initialize_chroma_db(chroma_db_path="chroma_db", db_name="Exotic_Option")

def querying_chromadb(query):
    """query chromadb for a list of genes"""
    query = convert_to_eng(query)
    docs = collection.query(
    query_texts=[query], 
    n_results=10, 
    )
    return docs

def format_docs(docs):
    """Format docs for display"""
    formatted_docs = []
    for idx, doc in enumerate(docs['documents'][0]):
        formatted_docs.append({
            "id": docs['ids'][0][idx],
            "page": docs['metadatas'][0][idx]['page'],
            "text": docs['documents'][0][idx],
            "doc_name": docs['metadatas'][0][idx]['doc_name'],
            "path_doc": docs['metadatas'][0][idx]['path_doc'],
        })
    return formatted_docs

def get_context(docs): 
    encoder = tiktoken.get_encoding("cl100k_base")
    context = ""
    max_context_size = 4096 
    if len(encoder.encode(context)) < max_context_size: 
        for idx, doc in enumerate(docs):
            context += f"{idx + 1}. {doc['text']}\n"
            context += f" Number: {idx + 1}\n"
            context += f"Document: {doc['doc_name']}\n"
            context += f"Page: {doc['page']}\n"
    return context



def get_final_sources_used(response, docs):
    response = response.replace(",", "")
    lines = response.splitlines()
    source_indices = set()
    final_sources = []

    for line in lines:
        numbers = re.findall(r'\d+', line)
        for n in numbers:
            source_indices.add(int(n))

    for i in sorted(source_indices):
        if 0 < i <= len(docs): 
            doc = docs[i - 1]
            doc['id'] = str(i)
            final_sources.append(doc)

    return final_sources

def generate_answer(query):    
    docs = querying_chromadb(query) 
    docs = format_docs(docs)
    context = get_context(docs)
    final_prompt = system_prompt.format(
    query=query,
    context=context
    )
    response = model.generate_content(final_prompt)
    response = response.text
    sources = get_final_sources_used(response, docs)
    return response, sources



