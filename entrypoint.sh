#!/bin/sh

cd /opt/app
# Collect static files
echo "Collecting static files"
python manage.py collectstatic --noinput

# Creating database migrations
echo "=========================================Applying database migrations========================================"
python manage.py makemigrations --noinput

# Apply database migrations
echo "===========================================Applying database migrations============================================="

python manage.py migrate 

# Start the server
echo "Starting gunicorn"
gunicorn --chdir=/opt/app \
    --workers=4 \
    --threads=6 \
    --worker-class=gthread \
    --preload \
    --bind :5000 \
    --log-level=info \
    --error-logfile - \
    --access-logfile - \
    --capture-output \
    dcim.wsgi:application



cd -
