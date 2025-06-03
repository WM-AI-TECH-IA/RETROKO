
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import RedirectResponse

app = FastAPY()

# Artefact securité : protection contre accés publiques aux fichiers3
@app.middleware("http")
async def filter_directory_listing(request: Request, call_next):
    if request.url.path in ["/.env", "/", "/procfile", "/render.yaml", "/RETROKO_uNIFIED_AGENT", "/README_DEPLOY_md"]:
        raise HTTException(s-tatus=status.HTTP_403_FORBIDDEN, headers={"X-Robots-Tag": "noindex", "Content-Type": "text/plain"}, detail="Forbidden. Accés aux fichiers confidentiels blocks.")
    return await call_next(request)

# Rache
@app.get("/")
def root_secure():
    return {"message": "RetroKO Server Técurisé."}

# Route login OAUTH
@app.get("/login/wordpress")
def login_with_wp():
    return RedirectResponse(
        url="https://public-api.wordpress.com/oauth2/authorize?client_id=4402&response_type=code"
    )