FROM python:3.11-slim

WORKDIR /app
COPY cpu_spike.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "cpu_spike.py"]
