from .base import *  # noqa
from .base import env

DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="",
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "192.168.0.2:3000"]

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
