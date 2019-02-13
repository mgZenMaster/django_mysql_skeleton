FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache mysql-client mysql-dev build-base
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
ADD docker-entrypoint.sh /
ADD waitfordb.py /
RUN chmod +x /waitfordb.py /docker-entrypoint.sh
RUN pip install -r requirements.txt
RUN cp /usr/lib/libmariadb.so.3 /tmp && apk del --purge mysql-dev build-base && mv /tmp/libmariadb.so.3 /usr/lib

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 8000
