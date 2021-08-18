FROM ubuntu:20.04
RUN apt-get -y update
RUN apt-get install python3 -y
WORKDIR /app
COPY client.py .
CMD ["client.py"]
ENTRYPOINT ["python3"]                            
