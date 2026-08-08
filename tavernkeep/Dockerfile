FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    zip \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . ./tavernkeep
COPY ../dashboard ./dashboard

# Set Python path
ENV PYTHONPATH=/app

EXPOSE 5000

CMD ["uvicorn", "tavernkeep.main:app", "--host", "0.0.0.0", "--port", "5000"]
