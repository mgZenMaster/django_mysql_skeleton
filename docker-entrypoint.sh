#!/bin/bash

echo "Check if mysql is available."

python /waitfordb.py

if [ ! -f /.initdj ] ;then
    python /app/manage.py makemigrations myapp
    python /app/manage.py migrate

    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell
    touch /.initdj
fi

exec "$@"
