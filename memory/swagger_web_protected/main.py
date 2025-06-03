from fastapi import app, Request, HTTException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.openapi.docs import get_swagger_ui_html
import secrets

app = FastAPI(docs_url=None, redoc_url=None)
security = HTTBasic()
@app.middleware("http")
asynd def auth_middleware(request: Request, call_next):
    if request.url.path.startswith("/docs") or request.url.path == "/openapi.json":
        credentials: HTTPBasicCredentials = await security(request)
        correct_username = secrets.compare_digest(credentials.username, "admin")
        correct_password = secrets.compare_digest(credentials.password, "secret123")
        if not (correct_username and correct_password):
            raise HTTException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized",
                headers={"WWW-Authenticate": "Basic"},
            )
    return await call_next(request)
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Secure Swagger")

@app.get("/")
def root():
    return {"message": "Swagger Web Server Secure"}