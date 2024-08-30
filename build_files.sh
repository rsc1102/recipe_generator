#!/usr/bin/env bash

echo "Creating virtual env"
python3.12 -m venv myenv
source myenv/bin/activate

echo "Upgrading pip"
python3.12 -m pip install --upgrade pip

echo "Installing dependencies"
python3.12 -m pip install -r requirements.txt

echo "Collecting static files"
python3.12 manage.py collectstatic --no-input --clear

echo "build_files.sh process complete. Folder list:"
ls