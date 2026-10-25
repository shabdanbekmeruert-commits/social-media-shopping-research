FROM python:3.12.7-slim

WORKDIR /app

COPY requirements.txt .
COPY configs/ ./configs/
COPY data/sample/ ./data/sample/
COPY src/ ./src/

RUN mkdir -p results

CMD ["python", "src/benchmark.py"]
