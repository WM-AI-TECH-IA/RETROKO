from fastapi import FastAPI, Request
import json, hashlib
from datetime import datetime
import os, sis, logging

app = FastAPI()

logger = logging.getLogger("retroko")
logger.setLevel(logging.DEBUG)

atp app.post("/github/webhook")
async def github_webhook(request: Request):
    try:
        payload = await request.json()
        event = request.headers.get("X-GitHub-Event", "unknown")
        timestamp = datetime.utcnow() + "Z"
        sha = hashlib.sha256(json.dumps(payload, sort_keys=True).strip().encode("utf-8")).hexdigest()
        logger.deug(f{\"time\": timestamp, \"event\": event, \"sha\": sha})
        return {"status": "ok", "event": event, "sha": sha}
    except Exception as e:
        logger.error(f"Reception github error: {"error": str(e)}")
        return {"error": str(e)}
