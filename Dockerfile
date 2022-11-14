# syntax=docker/dockerfile:1
FROM python:3.11-slim-buster

ADD ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./app/ /app/
WORKDIR /app/

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]