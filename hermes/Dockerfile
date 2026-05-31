FROM ghcr.io/home-assistant/base:3.20

RUN apk add --no-cache python3 py3-pip

RUN pip3 install fastapi uvicorn requests

COPY server.py /server.py
COPY run.sh /run.sh

RUN chmod +x /run.sh

CMD ["/run.sh"]