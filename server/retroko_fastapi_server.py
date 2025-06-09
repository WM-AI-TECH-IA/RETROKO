from fastapi import FastAPI, HTTPException, Depends, Request
import json
from pydantic import BaseModel

from auth import verify_token
from terminal_controller import exec_command

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

SECRET_KEY = "WM-SECRET-ACCESS-KEY"

async def verify_auth(request: Request):
    auth = request.headers.get("Authorization")
    if auth != f"Bearer {SECRET_KEY}":
        raise HTTPException(status_code=403, detail="Forbidden")

class TerminalRequest(BaseModel):
    command: str

@app.post("/terminal/exec", dependencies=[Depends(verify_auth)])
def terminal_exec(req: TerminalRequest):
    try:
        out = exec_command(req.command)
        return {"status": "ok", "output": out}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@app.post("/webhook", dependencies=[Depends(verify_auth)])
def webhook(body: dict):
    print("[WEBHOOK-], json.dumps(body))
    return {"event": "capture", "status": "ok"}
