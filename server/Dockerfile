FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY .. .

RUN ls -la /app

ENV PYTHONPATH=/app/backend
CMD ["python", "backend/server.py"]
