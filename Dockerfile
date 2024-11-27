FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements

COPY . .

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

EXPOSE 5000