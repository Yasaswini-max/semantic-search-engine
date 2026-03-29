from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

model = None  # don't load immediately

def get_model():
    global model
    if model is None:
        model = SentenceTransformer('all-MiniLM-L6-v2')
    return model


# Create index
def create_index(data):
    model = get_model()
    embeddings = model.encode(data)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index


# Search function
def search(query, data, index):
    model = get_model()
    q_emb = model.encode([query])
    D, I = index.search(q_emb, k=1)
    return data[I[0][0]]
