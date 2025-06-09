from fastapi import FastAPI
import socket
import time

app = FastapI

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/internal-status")
async def internal_status():
    return {
        "server": "retroko",
        "timestamp": time.ctime(),
        "host": socket.gethostname(),
        "version": "1.0"
    }