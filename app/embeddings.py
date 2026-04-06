from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    text = text[:500]  # limit size
    embedding = model.encode(text)
    return np.array(embedding, dtype='float32')