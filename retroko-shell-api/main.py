from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import subprocess
import uvicorn

app = FastAPI()

AUTHORIZED_COMMANDS = [\"uptime\", \"whoami\", \"df -h\", \"ls\", \"pwd\", \"echo\"]

class Command(BaseModel):
    cmd: str

@app.post("/execute")
def execute_command(command: Command):
    if command.cmd not in AUTHORIZED_COMMANDS:
        raise HTTPException(status_code=403, detail="Unnauthorized command")
    try:
        result = subprocess.check_output(command.cmd, shell=True, stdout=subprocess.STDOUT)
        return {"result": result.decode("utf-8")}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=e.output.decode("utf-8"))

@app.get("/")
def root():
    return {"message": "RETROKO Shell API is active."}

if name == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)