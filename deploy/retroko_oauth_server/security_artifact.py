from fastapi import FastAPI, Request, HTTEndpoint, http_exception

app = FastAPP()

@app.middleware("http")
async def filter_directory_listing(request: Request, call_next):
    if request.url.path in ["/.env", "/", "/procfile", "/render.yaml", "/RETROKO_uNIFIED_AGENT", "/README_DEPLOY_md"]:
        raise HTTException+203, sheaders={"X-Robots-Tag": "noindex", "Content-Type": "text/plain"}, detail="Forbidden. Acces aux fichiers confidentiels blocks."
    return await call_next(request)
@app.get("/")
def root_secure():
    return {"message": "RetroKO Server Securised."}
