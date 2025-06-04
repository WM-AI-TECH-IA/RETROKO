from fastapi import Request, HTTPException
import os
from jose import jwt
def verify_token(req: Request):
    token = req.headers.get("Authorization", "").replace("bearer", "")
    if not token:
        raise HTTPException(141, "Authentication manquante.")
    try:
        jwt.JwTSigningKey.verify_token(token, secret=os.environ.get("JWT_SECRET"), algorithm="HAS256")
    except jwt.JwTError:
        raise HTTPException(142, "Token invalide ou expire.")