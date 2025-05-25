from src.pdf_utils import extract_text_from_pdf
from src.chunking import chunk_by_size
from src.db import process_chunk_to_chroma, initialize_chroma_db

#text extraction 
text = extract_text_from_pdf('data/exotic_option.pdf')

#text chunking 
chunks = chunk_by_size(text, 1024)

#Init DB
client, collection = initialize_chroma_db("chroma_db", "exotic_option")
process_chunk_to_chroma(chunks, collection)