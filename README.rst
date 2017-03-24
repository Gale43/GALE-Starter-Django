GALE Starter Django
===================

This project lets you quickly kickstart a Django project.

Features
---------

* Virtualenv + Docker support
* Ready to be deployed using docker (for example to AWS ElasticBeanstalk)
* 12-Factor_ based settings via django-environ_
* Docker support using docker-compose_ for development and production
* Works with Python 3.5.x
* Run tests with unittest or py.test
* Customizable PostgreSQL version
* 


Constraints
-----------

* Only maintained 3rd party libraries are used.
* Uses PostgreSQL everywhere (9.2+)
* Environment variables for configuration (This won't work with Apache/mod_wsgi).


Usage
------

First, get Cookiecutter.

```
    $ pip install "cookiecutter>=1.4.0"
```
    
Then run it against this repo:

```
    $ cookiecutter https://github.com/Gale43/GALE-Starter-Django
``` 

You'll be prompted for some values. Provide them, then a Django project will be created for you. CD into the newly created directory and either prepare a virtualenv or run 

```
    $ docker-compose build
    $ docker-compose up
```
