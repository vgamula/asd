asd (Architectural service department)
==
Course prjects for managing ASD data. 
***

Installation
==
Install project with dependencies:
```
$ git clone git@github.com:vgamula/asd.git
$ cd asd
# use virtualenv for virtual environment
$ pip install -r requirements.txt
```

Create db schema:
```
$ cd asd
$ python manage.py syncdb
$ python manage.py migrate
```

Running server:
```
$ python manage.py runserver
```
Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
