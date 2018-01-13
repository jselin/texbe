#!/bin/sh
 
echo Collect static files
python manage.py collectstatic --clear --noinput 
python manage.py collectstatic --noinput  

echo Starting migrations
./wait-for.sh $DB_HOSTNAME:$DB_PORT --timeout=10 -- python3 manage.py migrate

echo Starting nginx
rm /etc/nginx/nginx.conf
cp nginx.conf /etc/nginx/nginx.conf
/usr/sbin/nginx 

echo Starting Gunicorn
gunicorn texbe.wsgi:application \
    --bind unix:/tmp/django_app.sock \
    --workers 3

