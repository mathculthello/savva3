FROM node:10 AS builder
WORKDIR /app
COPY package.json package-lock.json /app/
RUN npm install
COPY . .
RUN npm run build

FROM python:3.7.7
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# COPY FRONTEND
COPY --from=builder /app/static-dist static-dist
RUN ./manage.py collectstatic --no-input
CMD gunicorn --bind=0.0.0.0:8000 --chdir=/app --log-level=info --log-file=/dev/stdout savva3.wsgi
