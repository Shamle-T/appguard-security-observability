# Backend container placeholder
# This is the image file/creates docker image -> using this we can create multiple containers
# This tells Docker how to run your FastAPI backend.

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Used to run the docker file when we use ''
CMD ["uvicorn","app.main:app","--host", "0.0.0.0", "--port","8000"]

# When a container starts, docker executes: uvicorn app.main:app --host 0.0.0.0 --port 8000
