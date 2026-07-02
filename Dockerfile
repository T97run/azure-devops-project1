FROM python:3.11-slim

WORKDIR /app

# Copy and install dependencies first (helps with caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000 for local testing
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
