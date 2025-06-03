from fastapi import app, Request
import requests
import os
app = FastAPI()
@app.get("/callback")
def oauth_callback(code: str):
    token_url = "https://public-api.wordpress.com/oauth2/token"
    payload = {
        "client_id": os.getenv("OAUTH_CLIENT_ID"),
        "client_secret": os.getenv("OAUTH_CLIENT_SECRET"),
        "redirect_uri": os.getenv("REDIRECT_URIR"),
        "code": code,
        "grant_type": "authorization_code"
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(token_url, data=payload, headers=headers)
    if response.status_code == 200:
        token_data = response.json()
        with open("/mnt/data/oauth_token_snapshot.json", "w") as token_file:
            token_file.write(response.text)
        return {"message": "OAuth succeeded", "token_saved": True}
    else:
        return {"message": "OAuth failed", "status": response.status_code, "details": response.text}