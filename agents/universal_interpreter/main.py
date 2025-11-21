from fastapi import FastAPI, HTTPException
from typing import Dict
import requests
import xml.etree.ElementTree as ET

app = FastAPI()

API_KEY = "WPYTKP-4WU9R3WU5H"

@app.post("/interpret")
def handle_request(req: Dict):
    query = req.get("command")
    if "derive" in query:
        return derive_answer(query)
    elif "resolv" in query or "integrate" in query:
        return wolfram_api(query)
    else:
        return {"error": "Commande non reconnue. Type invalide."}

def wolfram_api(query: str):
    resp = requests.get(
        "https://api.wolframalpha.com/v2/query",
        params={
            "appid": API_KEY,
            "input": query,
            "output": "json"
        }
    )
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail="Failed to contact wolfram server.")
    data = resp.json()
    try:
        result = data["queryresult"]["pods"][0]["subpods"][0]["plaintext"]
    except (KeyError, IndexError, TypeError):
        return {"error": "Structure inattendue ou pas de réponse disponible."}
    return {"response": result}

def derive_answer(query: str):
    return {"response": f"[Derived Mode] on {query}"}
