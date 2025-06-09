from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import json

from auth import verify_token
from terminal_controller import exec_command

app = FastAPI()


class TerminalRequest(BaseModel):
    command: str


@app.post("/terminal/exec", dependencies=[Depends(verify_token)])
def terminal_exec(req: TerminalRequest):
    try:
        out = exec_command(req.command)
        return {"status": "ok", "output": out}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/webhook")
def webhook(body: dict):
    print("[WEBHOOK]", json.dumps(body))
    return {"event": "capture", "status": "ok"}
