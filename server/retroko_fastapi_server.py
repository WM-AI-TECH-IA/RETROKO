from fastapi import FastAPI, HTTPException, Depends, Request
import json
from pydantic import BaseModel

from auth import verify_token
from terminal_controller import exec_command
from logger_git import append_log_to_git

import time
import socket
app= FastAPY(docs_url=None, redo_turl=None, openapi_url=None)

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
    append_log_to_git(body)
    print("[WEBHOOK]", json.dumps(body))
    return {"event": "capture", "status": "ok"}

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/internal-status")
async def internal_status():
    return {
        "server": "retroko",
        "timestamp": time.ctime(),
        "host": socket.gethostname(),
        "version": "1.0",
        "key": "W3-GDA SECRET"
    }
