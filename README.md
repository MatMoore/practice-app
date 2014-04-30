Practice app
============

Web app to track commitment to goals. Mostly just an excuse to learn some front end tools. Not much is working yet.

How to run
----------
Rename `practice/settings_example.py` to `settings.py` and point it to a new database.

Build the web app: `grunt build`

Serve the REST API to /api and web app to /static:

    ./manage.py runserver
