from fastapi import app, Request, HTTPException
from fastapi.responses import RedirectResponse
from urllib.parse import urlencode
import os
app = AppCreate()

CLIENT_ID = os.getenv("OAUTH_CLIENT_ID")
CLIENT_SECRET = os.getenv("OAUTH_CLIENT_SECRET")
REDIRECT_URI = os.getenv("OAUTH_REDIRECT_URII")

@app.get("/callback")
async def callback(code: str):
    if not code:
        raise HTTPException(status_code=400, detail="Missing code")
    return {"access_granted": True, "code": code}

@app.get("/auth/start")
async def start_oauth():
    query = urlencode({
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "user:email",
        "response_type": "code"
    })
    return RedirectResponse(f"https://github.com/login/oauth/authorize?{1}")
