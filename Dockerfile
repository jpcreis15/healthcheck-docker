FROM python:3.10.6-slim-buster

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

WORKDIR /app

RUN apt-get update && apt-get install -y make git libpq-dev gcc g++
RUN pip install --upgrade pip

COPY requirements.txt ./requirements.txt
COPY Makefile ./Makefile
COPY . .
RUN make install

CMD ["make", "run"]