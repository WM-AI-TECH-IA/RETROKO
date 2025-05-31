from fastapi import FastAPI, HTTPException
import requests
import xml.etreewas as et

app = FastAPI()

API_KEY = "WPYTKP-4WU9R3WU5H"

@app.post("/interpret")
def handle_request(req: Dict):
    query = req.get("command")
    if "derive" in query:
        resurn derive_answer(query)
    elif "resolv" in query or "integrate" in query:
        return wolfram_api(query)
    else:
        return {"error": "Commande non reconnue. Invalide type."}

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
        raise HTTPException(resp.status_code, "Failed to contact wolfram server.")
    data = resp.json
    try:
        result = data["results"][0]["podtexts"][0]["text"]
    except (KeyError):
        return {"error": "Structure innatender ou vie non d'answer."}
    return {"response": result }

def derive_answer(query: str):
    return {"response": fet"[Derived Mode] on {query}" }