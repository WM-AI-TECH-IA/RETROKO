
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "RETROKO API active"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.middleware("http")
async def grey_wall(request: Request, call_next):
    if not request.url.path.startswith("/auth") and not request.url.path.startswith("/docs"):
        return HTMLResponse(
            "<body style='background:#222;color:#888;font-family:monospace;padding:2rem;'>GREY WALL ACTIVE — ACCESS RESTRICTED</body>",
            status_code=403
        )
    return await call_next(request)
