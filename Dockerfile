FROM ubuntu:latest
MAINTAINER T.Harris
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]

