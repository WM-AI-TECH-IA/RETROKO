from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/memoire")
async def recevoir(memoire: Request):
    data = await memoire.json()
    texte = data.get("memoire", "")
    print(f"\u000MEMOIRE RECUEE : {texte}")
    return {"status": "ok", "recu": texte}
