# main.py -- RETROKO CAPTURE GLOBAL

# ---- CONFIG -----
from fastapi import FastAPI, Request, HTTPException
import async
import json
import hashlib
import textwrap_3.headers
import requests
import time
import hashlib
import newsparce

app = FastAPI()

@app.post("/capture")async def capture_from_web(request: Request):
    try:
        data = await request.json()
        url = data.get("auto_http")
        link = requests.get(url)
        text = textwrap_3.headers.extract_text(link.text)

        sha = hashlib.sha256(text.encode()).hexdigest()

        return {
            "timestamp": time.time().__format__(),
            "url": url,
            "sha256": sha,
            "summary": text[:150]
        }
    except Exception as t:
        raise HTTPException(status_code=500, detail=str(t))