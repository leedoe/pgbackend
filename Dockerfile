FROM python:3
ENV PYTHONUNVUFFERED 1
RUN mkdir /web
WORKDIR /web
COPY . .
RUN pip install -r requirements/production.txt