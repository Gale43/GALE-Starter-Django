Cookiecutter Django
=======================

Features
---------

* For Django 1.11 LTS
* 12-Factor_ based settings via django-environ_
* Docker support using docker-compose_ for development and production
* Works with Python 3.5.x
* Run tests with unittest or py.test
* Customizable PostgreSQL version


Constraints
-----------

* Only maintained 3rd party libraries are used.
* Uses PostgreSQL everywhere (9.2+)
* Environment variables for configuration (This won't work with Apache/mod_wsgi).


Usage
------

Let's pretend you want to create a Django project called "redditclone". Rather than using `startproject`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter_ to do all the work.

First, get Cookiecutter. Trust me, it's awesome::

    $ pip install "cookiecutter>=1.4.0"

Now run it against this repo::

    $ cookiecutter https://github.com/Gale43/GALE-Starter-Django

You'll be prompted for some values. Provide them, then a Django project will be created for you.

**Warning**: After this point, change 'Daniel Greenfeld', 'pydanny', etc to your own information.

Answer the prompts with your own desired options_. For example::

    Cloning into 'cookiecutter-django'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.
    project_name [Project Name]: Django Demo
    project_slug [reddit_clone]: django_demo
    author_name [Daniel Roy Greenfeld]: GALE Partners
    email [you@example.com]: example@galepartners.com
    description [A short description of the project.]: A django projects.
    domain_name [example.com]: galepartners.com
    version [0.1.0]: 0.0.1
    Select postgresql_version:
    1 - 9.5
    2 - 9.4
    3 - 9.3
    4 - 9.2
    Select open_source_license:
    1 - MIT
    2 - BSD
    3 - GPLv3
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]: 1

Enter the project and take a look around::

    $ cd django_demo/
    $ ls

Create a git repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first awesome commit"
    $ git remote add origin git@github.com:Gale43/django-demo.git
    $ git push -u origin master

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?

For local development, see the following:

* `Developing locally`_
* `Developing locally using docker`_

.. _options: http://cookiecutter-django.readthedocs.io/en/latest/project-generation-options.html
.. _`Developing locally`: http://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html
.. _`Developing locally using docker`: http://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html

Community
-----------

* Have questions? **Before you ask questions anywhere else**, please post your question on `Stack Overflow`_ under the *cookiecutter-django* tag. We check there periodically for questions.
* If you think you found a bug or want to request a feature, please open an issue_.
* For anything else, you can chat with us on `Gitter`_.

.. _`Stack Overflow`: http://stackoverflow.com/questions/tagged/cookiecutter-django
.. _`issue`: https://github.com/pydanny/cookiecutter-django/issues
.. _`Gitter`: https://gitter.im/pydanny/cookiecutter-django?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

For Readers of Two Scoops of Django 1.8
--------------------------------------------

You may notice that some elements of this project do not exactly match what we describe in chapter 3. The reason for that is this project, amongst other things, serves as a test bed for trying out new ideas and concepts. Sometimes they work, sometimes they don't, but the end result is that it won't necessarily match precisely what is described in the book I co-authored.

Articles
---------

* `Development and Deployment of Cookiecutter-Django on Fedora`_ - Jan. 18, 2016
* `Development and Deployment of Cookiecutter-Django via Docker`_ - Dec. 29, 2015
* `How to create a Django Application using Cookiecutter and Django 1.8`_ - Sept. 12, 2015
* `Introduction to Cookiecutter-Django`_ - Feb. 19, 2016
* `Django and GitLab - Running Continuous Integration and tests with your FREE account`_ - May. 11, 2016

Have a blog or online publication? Write about your cookiecutter-django tips and tricks, then send us a pull request with the link.

.. _`Development and Deployment of Cookiecutter-Django via Docker`: https://realpython.com/blog/python/development-and-deployment-of-cookiecutter-django-via-docker/
.. _`Development and Deployment of Cookiecutter-Django on Fedora`: https://realpython.com/blog/python/development-and-deployment-of-cookiecutter-django-on-fedora/
.. _`How to create a Django Application using Cookiecutter and Django 1.8`: https://www.swapps.io/blog/how-to-create-a-django-application-using-cookiecutter-and-django-1-8/
.. _`Introduction to Cookiecutter-Django`: http://krzysztofzuraw.com/blog/2016/django-cookiecutter.html
.. _`Django and GitLab - Running Continuous Integration and tests with your FREE account`: http://dezoito.github.io/2016/05/11/django-gitlab-continuous-integration-phantomjs.html

Code of Conduct
---------------

Everyone interacting in the Cookiecutter project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.

Support This Project
---------------------------

This project is maintained by volunteers. Support their efforts by spreading the word about:

.. image:: https://s3.amazonaws.com/tsacademy/images/tsa-logo-250x60-transparent-01.png
   :name: Two Scoops Academy
   :align: center
   :alt: Two Scoops Academy
   :target: https://twoscoops.academy/

.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/
