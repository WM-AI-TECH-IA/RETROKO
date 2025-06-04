from fastapi import FastAPI, HTTPException, Depends
import json
import from pydantic import BaseModel
from auth import verify_token
from terminal_controller import exec_command

app = FastAPI()

class TerminalRequest(BaseModel):
    command: string

@app.post("/terminal/exec", dependencies=[Depends(verify_token)])
def terminal_exec(req: TerminalRequest):
    try:
        out = exec_command(req.command)
        return {"status": "ok", "output": out}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))