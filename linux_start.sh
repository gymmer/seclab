echo ===================================================
echo =============  DELETE OLD DATABASE  ===============
echo ===================================================
if [ -f "db.sqlite3" ]; 
	then rm db.sqlite3
fi

echo
echo
echo ===================================================
echo ================  MIGRATE DATABASE  ===============
echo ===================================================
python manage.py makemigrations
python manage.py migrate

echo
echo
echo ===================================================
echo ==================  IMPORT DATA ===================
echo ===================================================
echo Loading data from fatherMenu.json
python manage.py loaddata seclab/json/fatherMenu.json
echo

echo Loading data from sonMenu.json
python manage.py loaddata seclab/json/sonMenu.json
echo

echo Loading data from img.json
python manage.py loaddata seclab/json/img.json
echo

echo Loading data from article.json
python manage.py loaddata seclab/json/article.json
echo

echo
echo
echo ===================================================
echo ================  CREATE PASSWORD  ================
echo ===================================================
echo Create a password to manage the website...
python manage.py createsuperuser --username admin --email blank
echo Ok, Now you can use USERNAME:admin and the password to login!

echo
echo ===================================================
echo The login  URL is: http://ip:8080/admin
echo The seclab URL is: http://ip:8080/
echo ===================================================

echo
echo
echo ===================================================
echo ===================  RUN SERVER  ==================
echo ===================================================
nohup python manage.py runserver 0.0.0.0:8080 &
