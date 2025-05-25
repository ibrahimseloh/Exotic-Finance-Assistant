from .llm_utils import convert_to_eng, model
from prompt import system_prompt
from src.db import initialize_chroma_db
from prompt import system_prompt
import ast

client, collection = initialize_chroma_db(chroma_db_path="chroma_db", db_name="exotic_option")

def querying_chromadb(query):
    """query chromadb for a list of genes"""
    query = convert_to_eng(query)
    results = collection.query(
    query_texts=[query], 
    n_results=20, 
    )
    docs = list()
    for i in range(len(results['documents'][0])):
        d = {
            'id': results['ids'][0][i],
            'text': results['documents'][0][i],
        }
        docs.append(d)
    return docs

def generate_answer(query):    
    docs = querying_chromadb(query) 
    final_prompt = system_prompt.format(
    query=query,
    retrieved_docs=docs)
    response = (model.generate_content(final_prompt)).text
    response = response.split('```json')[1].split('```')[0].strip()
    bot_response = ast.literal_eval(response)
    return bot_response['bot_response']



