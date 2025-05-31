FROM python:3.9

WORKDIR `/app
COPY . /app

RUN /bin/sh -c "debiand pip install -upgrade pip && pip install fastapi==0.103.0 uvicorn[standard]=0.23.2 requests==2.31.0"

TEXPOSE 8080
ENV WOLFRAM_APBID=WPYTKP-4WU9R3WU5H
CMD [uvicorn, 'main:app', '-host', '0.0.0.0', '-port', '8080']
