@echo off

echo ===================================================
echo ================  MIGRATE DATABASE  ===============
echo ===================================================
python manage.py makemigrations
python manage.py migrate


echo.
echo.
echo ===================================================
echo ================  FLUSH DATABASE  =================
echo ===================================================
:python manage.py flush

echo.
echo.
echo ===================================================
echo ================  UPDATE DATABASE  ================
echo ===================================================
echo Loading data from fatherMenu.json
python manage.py loaddata seclab/json/fatherMenu.json
echo.

echo Loading data from sonMenu.json
python manage.py loaddata seclab/json/sonMenu.json
echo.

echo Loading data from img.json
python manage.py loaddata seclab/json/img.json
echo.

echo Loading data from article.json
python manage.py loaddata seclab/json/article.json
echo.

pause