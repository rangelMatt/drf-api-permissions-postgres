# Lab - Class 32

## Project:  Permissions & Postgresql

### Author: Matt Rangel

### Links and Resources

- [Django](https://www.djangoproject.com)
- [Docker](https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html)
- Morning Lecture

### Setup

To deploy locally:

- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `python manage.py runserver`
- `python -m pip install Django`
- `pip install djangorestframework`
- `pip freeze > requirements.txt`
- `docker compose run`
- `docker-compose up --build`
- `docker-compose run web python manage.py migrate`
- `docker-compose run web bash`
  - `exit`

### Tests

To initiate tests, run `python3 manage.py test`# django-models

I did postgres before I ran the tests. So unfortunately I wasn't able to run the tests with dqlite.
