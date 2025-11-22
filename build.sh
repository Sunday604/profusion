#!/usr/env bash
# Exit on error
set -o errexit

# modify this line as needed for your package manager
pip install -r requirements.txt
#convert static asset files
python manage.py collectstatic --noinput

#appy any outstanding database migrations
python manage.py migrate