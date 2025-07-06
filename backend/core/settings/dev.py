from .base import *     # noqa

DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "perfume_dev"),
        "USER": os.getenv("POSTGRES_USER", "perfume"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "perfume"),
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}
