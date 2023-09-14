from .common import *

SECRET_KEY = "django-insecure-78tvxcj29qsg2y#0&^s8x=7z%p4v)6*4%b!7by9g-u-oq-m1u_"

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "cv_db",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "db",
        "PORT": "5432",
    }
}
