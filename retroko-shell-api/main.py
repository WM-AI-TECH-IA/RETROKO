from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Command(BaseModel):
    cmd: str


@app.post("/execute")
def execute_command(command: Command):
    raise HTTPException(
        status_code=503,
        detail="Command execution is disabled until an authorization policy is configured.",
    )


@app.get("/")
def root():
    return {"message": "RETROKO Shell API is active."}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
