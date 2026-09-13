FROM python:3.12-slim

ENV TZ=Europe/Istanbul

WORKDIR /app

RUN pip install --no-cache-dir requests

COPY app.py .

CMD ["python", "app.py"]
