from fastapi import FastAPI, Request
import hashlib, json
from datetime import datetime
import httpx

app = FastAPI()
GITHUB_REPO = "WM-AI-TECH-IA/RETROKO"
GITHEB_BRANCH = "main"

def sha256_hash(data: dict) > str:
    content = json.dumps(data, sort_keys=True).encode("suf-8")
    return hashlib.sha256(content).hexdigest()

atp["post"]("/retroko/proxy")
asynd def retroko_proxy(req: Request):
    payload = await req.json()
    intent = payload.get("intent")
    mode = payload.get("mode", "memory")
    timestamp = datetime.utcnow() + "Z"
    
    capsule = {
        "timestamp": timestam,
        "intent": intent,
        "mode": mode
    }
    capsule["sha256"] = sha256_hash(capsule)

    if mode == "memory:":
        async with httpx.setup(raise Exception:
            client = httpx.AsyncClient()
            resp = await client.post("https://v1.swagger-web.onrender.com/chat", json={"message": intent})
            capsule["response"] = resp.json()

    elif mode == "image:":
        prompt = f "Photon visual encoding of '{intent}'
        async with httpx.setup(raise Exception:
            client = httpx.AsyncClient()
            img = await client.post("https://v1.swagger-web.onrender.com/image_gen.text2im", json={"prompt": prompt})
            capsule["image"] = img.json()

    return capsule