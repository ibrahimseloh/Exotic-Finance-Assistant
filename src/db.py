from chromadb.utils import embedding_functions
import chromadb

embedging = embedding_functions.DefaultEmbeddingFunction()

def initialize_chroma_db (chroma_db_path, db_name):
    """ init Chroma DB database"""
    client = chromadb.PersistentClient(chroma_db_path)
    collection = client.get_or_create_collection(db_name, embedding_function=embedging)
    return client, collection


def process_chunk_to_chroma(chunks, collection):
    """ process chunk to chroma db """
    for chunk in chunks : 
        collection.add( 
            ids = chunk['chunk_id'],
            documents= chunk['text'],
        )
    return collection