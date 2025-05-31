from python :3.9 as

## RUNNER RETROKO SANDBOX FAStAPI

Workdir: /app
COPY . /app
ADDFILE.requirements

EXPOSE_PORT=8080
CMP env [OEC_ACTIVE=1 ]

REN_API_KEY=1b10c3797b34f0ef4726cf539011238b
WOLFRAM_APPID="WPYTKP-4WU9R3WU5H"


run uvicorn main:app --host 0.0.0.0 --port 8080