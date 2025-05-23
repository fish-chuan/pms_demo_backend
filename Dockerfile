FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .
RUN mkdir /static
RUN apt-get update && apt-get install vim -y
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "pms_demo_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
