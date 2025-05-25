import google.generativeai as genai
import os

model = genai.GenerativeModel("gemini-1.5-flash")  
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def convert_to_eng(query): 
    query = (model.generate_content(f"""
    "Reformule la phrase suivante en anglais correct : \"{query}\". "
    "Ne renvoie **que** la traduction anglaise, sans mots en trop, sans explication ni ponctuation superflue.""")).text
    return query

