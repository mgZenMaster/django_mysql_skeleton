#!/bin/sh

echo "Check if mysql is available."

python /waitfordb.py

if [ ! -f /.initdj ] ;then
    python /app/manage.py makemigrations myapp
    python /app/manage.py migrate

    CU="from django.contrib.auth.models import User;"
    CU="${CU} User.objects.create_superuser('admin', 'admin@example.com', 'pass')"
    CU="${CU} if User.objects.filter(username='admin').count() == 0 else None"
    echo "${CU}" | python manage.py shell
    touch /.initdj
fi

exec "$@"
