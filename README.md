laborbook
=========

This is a python-django project. It is a base for creating a site for employers and employees
to find each other based on skills on specific areas and education.

Usually the site should be hosted on Heroku (http://www.heroku.com).

This is not a working site for any specific workarea. This is just a base on top of to build
a working site application. Look at and learn the source code, and develop your own.

#Development Environment Setup

You need to have the following installed:
 - Python 2.7
 - PIP
 - virtualenv (can be installed via `pip install virtualenv`)
 - PostgreSQL 9.3 (http://www.postgresql.org/download/)

Now in the directory where you keep your projects do:
```
git clone https://github.com/CSXM/laborbook.git
cd laborbook
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

You need to have a special `DATABASE_URL` system variable set in format
    DATABASE_URL=postgres://username:password@host:port/database
For example:
    export DATABASE_URL=postgres://me:mypass@localhost:5432/laborbook

For conveniency you want might create a shell script for this for example in `venv/bin/local_dev.sh` and source that as well after sourcing `venv/bin/activate`.

`DATABASE_URL` is needed only for local testing. If using Heroku database, do not set or remove the variable and Heroku's database will be used instead.

You need to have a special `LABORBOOK_SECRET_KEY` system variable with unique 50 characters long string. The variable name is fixed in `settings.py` and should be changed accordingly in your own project.

Now to create and migrate the database and create django admin superuser:
    python manage.py migrate
    python manage.py createsuperuser
Enter your name, email address and password twice.

You should now be able to run the built-in django server:
    python manage.py runserver
Or if django_extensions is listed in `ISTALLED_APPS` in `settings.py` you can run a better server for debugging purposes:
    python manage.py runserver_plus

You can now access the laborbook and its admin page in:
http://127.0.0.1:8000
http://127.0.0.1:8000/admin

