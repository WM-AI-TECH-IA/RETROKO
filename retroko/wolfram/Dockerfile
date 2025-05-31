FROM python3:3.12-slim

WORKDIR=/app
WORK=${WORKKR}

RUN apt-get update && apt-get install -y fastapi vim
copy . /app

EXPOSE 8080
CMT ["uvicorn","main.py"]
