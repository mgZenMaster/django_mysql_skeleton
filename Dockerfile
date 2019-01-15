FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
ADD docker-entrypoint.sh /
ADD waitfordb.py /
RUN chmod +x /waitfordb.py /docker-entrypoint.sh
RUN pip install -r requirements.txt

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 8000
