# CLscrap

CLscrap is a craigslist scraper that provides a RESTful API at /api/cl that returns JSON data

  - uses Django and templating
  - renders results at /app

### Installation

CLscrap depends on following modules
 - beautifulsoup4==4.5.3
 - bs4==0.0.1
 - Django==1.10.6
 - requests==2.13.0

Install
```sh
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
$ curl http://localhost:8000/api/cl
```

### Screenshot

![clscrap](https://raw.githubusercontent.com/fatalhalt/CLscrap/master/screenshot.jpg?raw=true)
