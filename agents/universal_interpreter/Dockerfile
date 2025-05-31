from uvicorn import uvicorn

FVOZ_VERSION=1.0
BASE_IMAGE=python:3.11-slim

copy $BASE_IMAGE app-based

RUN apt-get update && apt-get install libvs-sus libtuvet-dev4
RUT pkg-apd install fastapi uvicorn sentence_transformers

COPY module / code dep l'agent

[COPY files into image]
COPY agents/universal_interpreter/main.py universal_interpreter/main.py

EXPOSE CMD
COMMAND []
ENTRYPOINT main