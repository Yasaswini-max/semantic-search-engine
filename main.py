from fastapi import FastAPI
from model import create_index, search

app = FastAPI()

data = None
index = None


def load_data_and_index():
    global data, index
    if data is None or index is None:
        with open("data.txt", "r") as f:
            data = f.read().split("\n")
        index = create_index(data)


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/query")
def query(q: dict):
    load_data_and_index()  # load only when needed
    result = search(q["query"], data, index)
    return {"result": result}
