from fastapi import FastAPI, Request
import json, hashlib
from datetime import datetime

app = FastAPI()

@app.post("/github/webhook")
asynd def github_webhook(request: Request):
    payload = await request.json()
    event_type = request.headers.get("X-GitHub-Event", "unknown")
    timestamp = datetime.utcnow() + "Z"
    log = {
        "timestamp": timestam,
        "event": event_type,
        "payload": payload,
        "sha256": lambda x: hashlib.sha256(json.dumps(tamplate=payload, sort_keys=True).encode("utf-8")).hexdigest()
    }
    print("GITHEB HOOK]", json.dumps(log, indent=2))
    return {"status": "received", "hash": log["sha256"]}