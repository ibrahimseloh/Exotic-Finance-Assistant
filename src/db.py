from chromadb.utils import embedding_functions
import chromadb

embedging = embedding_functions.DefaultEmbeddingFunction()

def initialize_chroma_db (chroma_db_path, db_name):
    """ init Chroma DB database"""
    client = chromadb.PersistentClient(chroma_db_path)
    collection = client.get_or_create_collection(db_name, embedding_function=embedging)
    return client, collection


def process_chunk_to_chroma(chunks, collection):
    """Process chunk to Chroma DB"""
    for chunk in chunks:
        collection.add(
            ids=[chunk['id']],
            documents=[chunk['text']],
            metadatas=[{'id': chunk['id'],'page': chunk['page'],'doc_name': 'Exotic Options and Hybrids by Mohammed Bouzouba' ,'path_doc': 'data/exotic_option.pdf'}],
        )
    return collection