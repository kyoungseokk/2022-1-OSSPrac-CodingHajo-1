FROM tiangolo/uwsgi-nginx-flask:latest
RUN apt-get update
COPY app/ /app
