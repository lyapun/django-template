
My project template for bootstrapping django projects.

## How to use ##

django-admin.py startproject --template https://github.com/lyapun/django-template/zipball/master <<project_name>>

## What included ##

### reqirements.txt ###

With:

**django** - no comments.

**south** - for database migrations.

**psycopg2** - for postgresql support.

**Pillow** - for working with images.

**django-annoying** - for usefull helpers.

**Mock**, **factory_boy**, **webtest**, **django-webtest**, **django-nose**, **nose-progressive** - for efficient testing.

**django-debug-toolbar** - Almost for control count of sql queries.

### Makefile ###

I use this for creating usefull commands like ```make run``` except typing ```python manage.py runserver```.

####General commands:####

```make run``` - run test server.

```make test``` - run tests. You can specify test: ``` make test test=application.TestCase.test_case``` But you should write your application names to ```test``` paramater in Makefile.

```make syncdb``` - same as ```python manage.py syncdb```

```make initmigration app=application_name``` - init migrations for application using *south*.

```make schemamigration app=application_name``` - make new migration for application using *south*.

```make migrate``` - execute migrations using *south*. You can specify app.

```make shell``` - run django shell.

```make clean``` - delete all *pyc files from project.

### Project structure ###

1. Settings are divided into different files.
2. All applications from requirements.txt already included to ```INSTALLED_APPS```
3. Admin enabled in urls by default.
4. Folders for templates, public, static.

### Links for reading ###

[A Humane Python Test Runner](http://blog.mozilla.org/webdev/2011/04/14/a-humane-python-test-runner/)
