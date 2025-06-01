from fastapi import FastAPI, Request, HTTPException
import textwrap
import time
import hashlib
import requests

app = FastAPI()

@app.post("/")
async def llm_proxy(request: Request):
    try:
        data = await request.json()

        if "auto_http" in data:
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

        return {"status": "OK", "detail": "LLM proxy active"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))