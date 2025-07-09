FROM python:3.12-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set settings explicitly for collectstatic (safe for production)
RUN DJANGO_SETTINGS_MODULE=core.settings.prod python manage.py collectstatic --noinput

CMD ["gunicorn", "core.wsgi:application", "-b", "0.0.0.0:8000"]
