FROM python:rc-alpine3.7
ENV PYTHONUNBUFFERED 1

RUN apk add --update python3-dev py3-pip gcc musl-dev && rm -rf /var/cache/apk/*
#RUN set -xe \
#    && apt-get update \
#    && apt-get install build-essential \
#    python-pip \
#    liblircclient-dev \
#    lirc
RUN pip install --upgrade pip
RUN pip install Django==2.1.1
RUN pip install gunicorn
RUN pip install pyyaml ua-parser user-agents
RUN pip install django-user-agents
RUN pip install djangorestframework
RUN pip install django-sslserver
RUN pip install django_crontab
RUN pip install django-choices
RUN pip install python-lirc
RUN pip install py_irsend
RUN pip install pyHS100

# RUN pip install -r ../src/requirements.txt

RUN mkdir -p /var/www/html
WORKDIR /var/www/html

CMD gunicorn --bind=0.0.0.0:8000 --workers=1 app.wsgi
