from fastapi import FastAPI, Request, HTTPException
import textwrap
import time
import hashlib
import requests

app = FastAPI()

@app.post("/capture")
async def capture_from_web(request: Request):
    try:
        data = await request.json()
        url = data.get("auto_http")
        link = requests.get(url)
        text = textwrap.shorten(link.text, width=150, placeholder="...")

        sha = hashlib.sha256(text.encode()).hexdigest()

        return {
            "timestamp": time.time(),
            "url": url,
            "sha256": sha,
            "summary": text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))