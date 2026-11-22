
FROM python:3.13-slim

WORKDIR /app

# Prevent Python from creating unnecessary cache files
ENV PYTHONDONTWRITEBYTECODE=1

# Show Python logs immediately
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application source files
COPY app.py .
COPY database.py .
COPY model.py .
COPY customer_schema.py .
COPY lead_scoring.py .

# Run application as a non-root user
RUN useradd --create-home appuser

USER appuser

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
