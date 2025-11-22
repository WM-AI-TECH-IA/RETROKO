from fastapi import Request, HTTPException
import os
from jose import jwt, JWTError

def verify_token(req: Request):
    auth_header = req.headers.get("Authorization", "")
    token = auth_header.replace("Bearer ", "").replace("bearer ", "").strip()
    if not token:
        raise HTTPException(status_code=401, detail="Authentication manquante.")
    try:
        payload = jwt.decode(token, os.environ.get("JWT_SECRET", ""), algorithms=["HS256"])
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f"Token invalide ou expiré: {str(e)}")
