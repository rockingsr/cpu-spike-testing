FROM python:3.11-slim

WORKDIR /app

# FIX: Add ENV to ensure logs are unbuffered for better observability in containers.
ENV PYTHONUNBUFFERED=1

COPY app.py

# FIX: Use --no-cache-dir to keep image smaller and build time faster; avoid caching wheel files.
RUN pip install --no-cache-dir fastapi uvicorn

# FIX: Expose 8000 to declare port mapping for container orchestrators and health checks.
EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]