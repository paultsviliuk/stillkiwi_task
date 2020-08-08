# Steelkiwi Python Test Task

[![steelkiwi](https://img.shields.io/badge/steelkiwi-black?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAAAAABWESUoAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAB3RJTUUH4QwFDCoN+yI2RQAAAAJiS0dEAP+Hj8y/AAABd0lEQVQ4y9WTzStEYRTGh5z3PcfnAguSmWyU1EgRu2HJYhpKSVEKGUZD0lioWYwsiSkLxX9gpaylyNKGRpr1yMLHRNz5eCzuvTNXDdZ+2/Or87zn6XXJH7j+jcDkQJsDRURsCdzinyjSwSLCVUPB4Ewbi7hE2HNq5ArkF0lE10We8L7VYAo0lYWDEIluin/gebXGWkFh4CYasVjv1ar9OIfUdCVbIWkZWCkvhlT9F0AyoAuvoGVgluxnMfsTwPWgkm/CnC1w9fwD8DhIUlrQ9bE0gExYO4XFt/S0KXDzoYHPRAb3XscK9gz4WllERGgyi4/trivgoMZxalbKnAsFgf26irE0XvyqVFkUBBYqpPYQOGvmH4QQifLeIbumC4IuHKlsCQiRiAoZSHYrO2TnSMBi/NwUuPEEOKq1u9jIGRYZID9DIqJ8KbyOKkuIOsu89Zq7Y3lcus269XB812Zvs88Mr92x+E6Ptu6giyj7xqy1/l8f5ze+AIGTzdfyz0XyAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDE3LTEyLTA1VDEyOjQyOjEzKzAxOjAweKsLygAAACV0RVh0ZGF0ZTptb2RpZnkAMjAxNy0xMi0wNVQxMjo0MjoxMyswMTowMAn2s3YAAABXelRYdFJhdyBwcm9maWxlIHR5cGUgaXB0YwAAeJzj8gwIcVYoKMpPy8xJ5VIAAyMLLmMLEyMTS5MUAxMgRIA0w2QDI7NUIMvY1MjEzMQcxAfLgEigSi4A6hcRdPJCNZUAAAAASUVORK5CYII=)](https://steelkiwi.com/)

You must develop a small REST API service that facilitates redirection to third-party resources. The purpose of this service is to collect information that may be needed for statistical analysis and to perform redirection.

The service does not provide any user authorization or actions related to it.

The estimated time to complete the task is from 3 to 4 hours.

## Start Project

### Prerequisites

Make sure to have the following on your host:

- Python >= 3.7
- PostgreSQL >=10
- git

### Setting Up Development Environment

Clone this repo:

```bash
$ git clone <repo url>
```

Create a virtualenv:

```bash
$ python3 -m venv <virtual env path>
```

Activate the virtualenv you have just created:

```bash
$ source <virtual env path>/bin/activate
```

Install requirements:

```bash
$ pip install -r requirements.txt
```

Create a new PostgreSQL database using `createdb`:

```bash
$ createdb steelkiwi_python_test_task -h localhost -U postgres
```

Create a file with environment variables:

```bash
$ cp env.example .env
or
$ touch env.example
```

Apply migrations:

```bash
$ python manage.py migrate
```

Run Celery:

```bash
$ celery -A config worker -l=info
```

Run development server:

```bash
$ python manage.py runserver
```
