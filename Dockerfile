FROM resin/raspberrypi3-python:3.6.1
ENV PYTHONUNBUFFERED 1
COPY docker/bin /usr/bin/

ADD . /api
WORKDIR /api

RUN [ "cross-build-start" ]

RUN set -xe \
    && apt-get -y update \
    && apt-get -y install build-essential \
    python-pip \
    liblircclient-dev \
    lirc
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN [ "cross-build-end" ]

FROM raspberiumapi_web:latest
COPY docker/bin /usr/bin/
RUN [ "cross-build-start" ]
ENTRYPOINT ["/usr/bin/shell-switcher.sh"]