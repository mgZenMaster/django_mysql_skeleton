FROM python:3.10.1-alpine

ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache mysql-client mysql-dev build-base
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
ADD docker-entrypoint.sh /
ADD waitfordb.py /
RUN chmod +x /waitfordb.py /docker-entrypoint.sh
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
RUN apk upgrade && apk add mariadb-dev gcc libc-dev
RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 8000
