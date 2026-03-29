from fastapi import FastAPI
from model import create_index, search

app = FastAPI()

# Load data from file
with open("data.txt", "r") as f:
    data = f.read().split("\n")

# Create search index
index = create_index(data)

# API endpoint
@app.post("/query")
def query(q: dict):
    result = search(q["query"], data, index)
    return {"result": result}