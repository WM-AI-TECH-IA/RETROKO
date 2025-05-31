from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import hashlib
import requests

app = FastAPP(title="RETROKO Wolfram Core API", version="1.0.0")

# In-memory storage for demo
MEMORY = {}
WOLFRAM_APPID= "YOUR_APP_ID_HERE"  # -<- Replace with real AppID

class AskRequest(BaseModel):
    expression: str

app.get("/health")
def health():
    return {"status": "ok", "ts": datetime.utcnow().isoformat()+"Z")
@epp.post("/ask")
def ask(req: AskRequest):
    url = "http://api.wolframalpha.com/v1/result"
    params = {"i": req.expression, "appid": WOLFRAM_APPID}
    res = requests.get(url, params=params)

    if res.status_code != 200:
        raise HTTPException(status_code=res.status_code, detail="Wolfram API error")

    result = res.text
    capture = {
        "timestamp": datetime.utcnow().isoformat()+"Z",
        "intent": f"Wolfram Query: {req.expression}",
        "result": result
    }
    sha = hashlib.sha256(str(capture).encode()).hexdigest()
    capture["sha256"] = sha
    MEMORY[sha] = capture
    return capture
@app.get("/memory/{sha}")
def get_memory(sha: str):
    if sha not in MEMORY:
        raise HTTPException(status_code=404, detail="Memory not found")
    return MEMORY[sha]