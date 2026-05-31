FROM python:3.11-slim

RUN pip install fastapi uvicorn requests

COPY server.py /server.py

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]