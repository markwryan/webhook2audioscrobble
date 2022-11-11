FROM ubuntu 

RUN apt-get update 
RUN apt-get install python3-pip -y
RUN pip3 install flask

COPY ./app/ /app/
WORKDIR /app/

EXPOSE 5000

ENTRYPOINT ["python3.10"]
CMD ["app.py"]