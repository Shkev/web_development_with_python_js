# Lecture 3: Django

* Create a new Django project using the `django-admin startproject PROJECT_NAME` command
* Start a server and run the website with `python3 manage.py runserver`
* Apps in Django are like sub-functions are the overarching website (ex: Google is the main site and Google Search and Images are the Apps within it.)
* Create a new app using `python3 manage.py startapp APP_NAME`
* Django has built in support for forms/inputs with the forms module
  * import using `from django import forms`
  * see views.py in the tasks app for an example

## Files

### Views

* Views.py file contains the views that the user will see on the site.
  * Each view is defined as a function
* html files can be rendered using the `render` function in django
  * files being rendered must be inside a folder called "templates"

### URLs

* urls.py file contains the urls that are contained in the site.
* urls.py in each app contains urls that can be accessed in each app
  * urls in the apps are linked to the main site using the main urls.py file

### HTML File Inheritance

* A layout file is created. The areas of the layout that will change are enclosed with `{% block BLOCKNAME %}` and `{% endblock %}`
* The `{% extends "file path" %}` is used to inherit the html code at the given path
* A `{% block BLOCKNAME %}` is then included in the inheriting file. The block is ended with `{% endblock %}`
  * All code is copied from the given layout file
  * The block areas in the layout file are replaced with the blocks given in the inheriting file

## Folders

* The **static directory** stores files that do not change (ex: css files, html files without conditions, etc.)
* The **templates directory** stores the files that represent the different sites on the website
  * These files can change (like html files with `if` conditions

## Sessions

* Allows different users to have their own variables as opposed to having global variables.
  * ex: For list of tasks, each user will have their own list instead of the same list being shown to each user
* The session variables are accessed with `request.session['VAR_NAME']`
