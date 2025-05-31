FROM python:3.9

WORKDIR `/app
COPY . /app

RUN pip install
RUN pip install -upgrade pip 
 && pip install fastapi==0.103.0 uvicorn[standard]==0.23.2 requests==2.31.0

ENV WOLFRAM_APBID=WPYTKP-4WU9R3WU5H

EXPOSE 8080
CMD [uvicorn, "main:app", "-host", "0.0.0.0", "-port", "8080"]
