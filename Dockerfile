FROM python:3.10.8-alpine3.15

ENV FLASK_APP=rest

ENV PORT=5000

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY rest /opt/rest

WORKDIR /opt

EXPOSE $PORT

CMD flask run --host 0.0.0.0 -p $PORT