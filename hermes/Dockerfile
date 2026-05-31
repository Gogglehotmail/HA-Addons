FROM ghcr.io/home-assistant/addon-base:17.0.0

RUN apk add --no-cache python3 py3-pip

RUN pip3 install fastapi uvicorn requests

COPY server.py /server.py
COPY run.sh /run.sh

RUN chmod +x /run.sh

CMD ["/run.sh"]