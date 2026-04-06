import faiss
import numpy as np
from app.embeddings import get_embedding
from app.reranker import rerank

documents = []
embeddings_list = []


def chunk_text(text, chunk_size=300, overlap=50):
    chunks = []
    
    for i in range(0, len(text), chunk_size - overlap):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks


def add_document(text):
    chunks = chunk_text(text)

    for chunk in chunks:
        
        if len(chunk.strip()) < 50:
            continue

        embedding = get_embedding(chunk)

        documents.append(chunk)
        embeddings_list.append(embedding)


def search(query, k=5):
    if not embeddings_list:
        return "No documents uploaded yet."

    
    query_embedding = get_embedding(query)

    embeddings_array = np.array(embeddings_list).astype('float32')
    query_array = np.array([query_embedding]).astype('float32')

    dim = embeddings_array.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(embeddings_array)

    D, I = index.search(query_array, k=k)

    retrieved_docs = [documents[i] for i in I[0]]

    
    top_docs = rerank(query, retrieved_docs)

    
    combined = " ".join(top_docs)

    
    sentences = combined.split('.')
    unique_sentences = list(dict.fromkeys(sentences))

    final_text = ". ".join(unique_sentences)

    return final_text