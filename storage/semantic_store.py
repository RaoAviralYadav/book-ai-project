import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("chapters")

def store_semantic_version(id, text):
    try:
        collection.delete(ids=[id])
    except Exception:
        pass
    collection.add(ids=[id], documents=[text])


def query_semantic_versions(query_text, n_results=5):
    """Return top-n semantically similar versions."""
    results = collection.query(
        query_texts=[query_text],
        n_results=n_results
    )
    return results
