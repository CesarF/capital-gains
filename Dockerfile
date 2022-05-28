FROM python:3.8.13-slim
RUN ["mkdir", "/capital"]
WORKDIR /capital
COPY main.py requirements.txt ./
COPY ./app ./app
COPY ./tests ./tests
RUN ["pip", "install", "-r", "requirements.txt"]