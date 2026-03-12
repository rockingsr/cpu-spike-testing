FROM python:3.11-slim

# FIX: Create a non-root user and run container as non-root for security and to align with best practices
RUN useradd -m appuser
# Set working directory for app
WORKDIR /app
# Copy application source
COPY app.py .
# FIX: Install runtime dependencies with no-cache to reduce image size and avoid cache-related drift
RUN pip install --no-cache-dir fastapi uvicorn
# FIX: Expose port for container orchestration visibility
EXPOSE 8000
# FIX: Run as non-root user
USER appuser

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
