
# Use a fixed Python version
FROM python:3.12.7-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY requirements.txt .
COPY configs/ ./configs/
COPY data/sample/ ./data/sample/
COPY src/ ./src/

# Create the results folder
RUN mkdir -p results

# Run the benchmark
CMD ["python", "src/benchmark.py"]
