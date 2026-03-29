from fastapi import FastAPI
from model import create_index, search

app = FastAPI()

data = None
index = None

# Load data and index only when needed
def load_data():
    global data, index
    if data is None or index is None:
        with open("data.txt", "r") as f:
            data = f.read().split("\n")
        index = create_index(data)


# Root endpoint (VERY IMPORTANT for Render)
@app.get("/")
def home():
    return {"status": "running"}


# Search endpoint
@app.post("/query")
def query(q: dict):
    load_data()  # lazy loading
    result = search(q["query"], data, index)
    return {"result": result}
