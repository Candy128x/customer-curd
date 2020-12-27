# Note Command's 


---
## Create Virtual Environment
- => virtualenv venv
- OR
- => virtualenv -p python3.8 venv


---
## Install pip Package's
- => pip install django
- => pip install djangorestframework
- => pip install psycopg2-binary


---
## Django Command's

> - create project
> > => django-admin startproject projdemo

> - create app
> > => python manage.py startapp sample_app

> - enable runserver
> > => python manage.py runserver

> - Create migration
> > => python manage.py makemigrations
> - Run migration
> > => python manage.py migrate

> - create Super User
> > => python manage.py createsuperuser

> - To open Interactive Console / Terminal 
> > => python3 manage.py shell

> DB data copy into JSON file
> - Syntax: python manage.py dumpdata app_name.model_name > app_name/fixtures/model_name.json
> > => python manage.py dumpdata customer.CustomerInfo > customer/fixtures/customer_info.json

> JSON data copy into DB
> - Syntax: python manage.py loaddata app_name/fixtures/model_name.json
> > => python manage.py loaddata customer/fixtures/customer_info.json




