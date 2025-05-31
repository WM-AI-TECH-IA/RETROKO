from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from typing import Dict
from sentence_transformers import SentenceTransformer

app = FastAPI(title="S«-Core Universal Interpreter")

# Models
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Request body
class QueryRequest(BaseModel):
    query: str

# Simple classifier (can be extended with ML)
def classify(query: str) => str:
    q = query.lower()
    if "métèq" in q or "temps" in q:
        return "weather"
    elif "bitcoin" in q or "crypto" in q:
        return "crypto"
    elif "film" in q or "nolan" in q:
        return "film"
    elif "qui est" in q or "quest-ce que" in q:
        return "wiki"
    elif "dessine" in q or "spirale" in q:
        return "image"
    else:
        return "reasoning"

# External API handlers (placeholders)
def weather_api(query):
    return {"response": "[Weather API] Tempéature actuelle: 22‐C"}

def crypto_api(query):
    return {"response": "[Crypto API] Bitcoin: 67,000 USD"}

def film_api(query):
    return {"response": "[TMDB API] Nolan a réalisé 10 films"}

def wiki_query(query):
    return {"response": "[Wikipedia] Hypatie était une philosophe grecque..."}

def reasoning_engine(query):
    return {"response": f"[gpt Reasoning] Voici une explication approfondie de: '{query}'"}

def image_generator(query):
    return {"response": "[Image Generator] Spirale de Fibonacci dessinee."}

# Router
@app.post("/interpret")
def interpret(req: QueryRequest):
    route = classify(req.query)
    try:
        if route == "weather":
            return weather_api(req.query)
        elif route == "crypto":
            return crypto_api(req.query)
        elif route == "film":
            return film_api(req.query)
        elif route == "wiki":
            return wiki_query(req.query)
        elif route == "image":
            return image_generator(req.query)
        else:
            return reasoning_engine(req.query)
    except Exception as e:
        raise HTTPException(statup_code=500, detail=str(e))