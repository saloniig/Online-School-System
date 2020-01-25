# Online School System Using Django

In this project there is an online `School System` where teachers can create assignments, upload study material and previous year papers that students can view. By this project you will get to know a lot about the Rest framework of django and also some amount of `Javascript` In this project `AJAX LIVE SEARCH ` is also used that displays the result as typed by the student .
# About Django 
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
## Features

-   A split of  `settings.py`  that allows for different values in  development  versus  production
-   Preinstallation of Django's  automatic administration panel
-   Preconfiguration of  `urls.py` to serve static, media and Munin files
-   Preconfiguration of  logging options
-   Preinstallation of  django-debug-toolbar
-   Preconfiguration of our preferred caching options for  development  and  production
-   Management commands for scheduling  database backups retrieving them for local installation.
-   Custom context processors that provide the  current site  and  environment


## Requirements

-   [Django](https://www.djangoproject.com/download/)
-   [virtualenv](http://www.virtualenv.org/en/latest/)



# Getting started

## Table of Contents

-   [Part 1 - Getting Started](https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html)
-   [Part 2 - Fundamentals](https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html)
-   [Part 3 - Advanced Concepts](https://simpleisbetterthancomplex.com/series/2017/09/18/a-complete-beginners-guide-to-django-part-3.html)
-   [Part 4 - Authentication](https://simpleisbetterthancomplex.com/series/2017/09/25/a-complete-beginners-guide-to-django-part-4.html)
-   [Part 5 - ORM](https://simpleisbetterthancomplex.com/series/2017/10/02/a-complete-beginners-guide-to-django-part-5.html)
-   [Part 6 - Class-Based Views](https://simpleisbetterthancomplex.com/series/2017/10/09/a-complete-beginners-guide-to-django-part-6.html)
-   [Part 7 - Deployment](https://simpleisbetterthancomplex.com/series/2017/10/16/a-complete-beginners-guide-to-django-part-7.html)

For the complete tutorial series index  [click here](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/).




# Installation
Please check the official django  installation guide for server requirements before you start. Official Documentation

## Setup
Create a virtual enviroment to work inside.

`virtualenv my-environment`

Jump in and turn it on.

`cd my-environment`

`. bin/activate`

### Install Django:

`pip install Django`

### Perform database migration:

`python manage.py makemigrations`

`python manage.py migrate`

### Run Development Server

`python manage.py runserver`

You can now access the server at http://localhost:8000

## Project File/Folder Structure

What I’ve changed ?

-   All Django apps live under  `mysite/`  folder.
-   All of the models live under  `models.py`  file.
-   All of the admin files live under  `admin.py`  file.
--   All of the views live under generated app’s  `views/`  folder.
-   Every app should contain It’s own  `urls.py`.
-   All settings related files will live under  `settings.py`  file.
-   Every environment has It’s own setting such as  
-   Every environment/settings can have It’s own package/module requirements.
-   All of the templates live under basedir’s  `templates/APP_NAME`  folder.
-   Additional files such as images, JavaScript, or CSS are live under `static/mine` folder.
-    Every environment/settings can have It’s own package/module requirements.

#### Here is directory/file structure:
```none


mysite/
    manage.py
    mysite/
       __init__.py
       settings.py
       urls.py
       wsgi.py
    mine/
       migrations/
               __init__.py
       __init__.py
       admin.py
       static
       templates
       models.py
       tests.py
       views.py
```


## Documentation

You can see the documentation over at  **Read the Docs**:  [django-project-skeleton](http://django-project-skeleton.readthedocs.org/en/latest/)
