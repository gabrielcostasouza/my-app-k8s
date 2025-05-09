FROM python:3.10-slim

WORKDIR /app

COPY app.py .
COPY requirements.txt .

RUN pip install --no-cache-dir flask flask-cors

EXPOSE 5000

CMD ["python", "app.py"]
