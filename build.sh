#!bin/bash

#Create a virtual env
echo "creating virtual env..."
python -m venv venv
source venv/bin/activate

echo "Installing the latest version of pip..."
python -m pip install --upgrade pip

echo "Building the project..."
python -m pip install -r requirements.txt

echo "Making migrations..."
python manage.py makemigrations --noinput

python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear


