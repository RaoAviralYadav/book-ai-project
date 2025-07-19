import chromadb


client = chromadb.Client()
collection = client.get_or_create_collection("chapters")

def store_semantic_version(id, text, metadata=None):
    
    try:
        collection.delete(ids=[id])
    except Exception:
        pass

    if metadata and isinstance(metadata, dict) and metadata:
        collection.add(ids=[id], documents=[text], metadatas=[metadata])
    else:
        collection.add(ids=[id], documents=[text])


def query_semantic_versions(query_text, n_results=5):
    
    results = collection.query(
        query_texts=[query_text],
        n_results=n_results
    )
    return results  