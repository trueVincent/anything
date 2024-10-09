FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq-dev gcc

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN mkdir -p /app/logs /app/media /app/static

# Collect static files
RUN python manage.py collectstatic --noinput

# Not running migrate here cause not in the same network with db when build the image.
# RUN python manage.py migrate

EXPOSE 8000

# gunicorn -c gunicorn_config.py todo.wsgi:application
CMD ["gunicorn", "-c", "gunicorn_config.py", "todo.wsgi:application"]