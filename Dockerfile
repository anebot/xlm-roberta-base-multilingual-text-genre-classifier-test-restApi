# syntax=docker/dockerfile:1

## docker build -t roberta-api .
## docker run -ti -p 8080:80 --name roberta-api-02 roberta-api

FROM python:3.10-slim-buster
LABEL maintainer="Artur Nebot"

RUN apt-get update
RUN pip install --upgrade pip
RUN apt install -y curl

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 80

ENV FLASK_RUN_PORT 80

COPY roberta-api.py .

CMD [ "flask", "--app", "roberta-api.py", "run","--host","0.0.0.0"]
