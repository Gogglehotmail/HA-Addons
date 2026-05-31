FROM python:3.11-slim

RUN pip install fastapi uvicorn requests

COPY server.py /server.py

CMD ["python", "/server.py"]