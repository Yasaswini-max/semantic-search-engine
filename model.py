from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# Load model (this converts text → numbers)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create index (store all data)
def create_index(data):
    embeddings = model.encode(data)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index

# Search function
def search(query, data, index):
    q_emb = model.encode([query])
    D, I = index.search(q_emb, k=1)
    return data[I[0][0]]