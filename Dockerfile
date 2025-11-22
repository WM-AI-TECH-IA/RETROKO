FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8080
ENV WOLFRAM_APPID=WPYTKP-4WU9R3WU5H
CMD ["uvicorn", "server.retroko_fastapi_server:app", "--host", "0.0.0.0", "--port", "8080"]
