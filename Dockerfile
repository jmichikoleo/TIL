# Use Python 3.11 slim image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy requirements and source
COPY requirements.txt .
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose container port
EXPOSE 5000

# Use entrypoint that reads .env variables
CMD ["sh", "-c", "export $(cat .env | xargs) && python app.py"]