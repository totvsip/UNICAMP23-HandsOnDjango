#bash
rm db.sqlite3
rm -rf app/migrations
./manage.py makemigrations
./manage.py makemigrations app
./manage.py migrate
./manage.py shell -c "from app.models import Usuario; Usuario.objects.create_superuser('admin', 'admin@example.com', 'admin')"
