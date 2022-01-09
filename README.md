# SmartCow Assessment

Completed by Nicholas Hoo on 9 January 2022, for more info check screenshots included in repo.

# How to get it running
- Clone to directory from GitHub repo https://github.com/n1ck940712/smartcow
- Below is the exact lines of code for me to get it running on a fresh machine
```
git clone https://github.com/n1ck940712/smartcow smartcow

cd smartcow

virtualenv -p python3.8 env

source env/bin/activate 

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```
- Visit localhost:8000/
- Create account and login

# Specifications
 - Framework: Django 
 - platform: Ubuntu 20.04 
 - database: sqlite 
 - annotate plugin: annotorious-2.4.0
