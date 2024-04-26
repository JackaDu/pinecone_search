from fastapi import FastAPI
from index import search
app = FastAPI()

@app.get("/search/{word}")
def find_companies(word: str):
    return {
        "res": search(word)
    }
