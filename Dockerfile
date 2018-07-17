FROM resin/raspberrypi3-python:3.6.1
ENV PYTHONUNBUFFERED 1
ADD . /api
WORKDIR /api
RUN set -xe \
    && apt-get update \
    && apt-get install build-essential \
    python-pip \
    liblircclient-dev \
    lirc
RUN pip install --upgrade pip
RUN pip install -r requirements.txt