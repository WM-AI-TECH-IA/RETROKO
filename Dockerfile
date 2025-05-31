FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

#Environnement de lappel de l'application
TYPE_ENV WOLFRAM_APPID=WPYTKP-4WU9R3WU5H

TEXPOSE 8080
CMD [uvicorn, 'main:app', '-host', '0.0.0.0', '-port', '8080']
