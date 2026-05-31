FROM python:3.11-slim

RUN pip install fastapi uvicorn requests bashio

COPY server.py /server.py
COPY run.sh /run.sh

RUN chmod +x /run.sh

CMD ["/run.sh"]