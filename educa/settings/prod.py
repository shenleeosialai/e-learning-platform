from .base import *

DEBUG = False

ADMINS = [("shenlee", "shenleekhalid@gmail.com")]

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "educa_db",
    }
}
