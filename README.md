[![PyPI](https://img.shields.io/pypi/v/django-sandstorm.svg)](https://pypi.python.org/pypi/django-sandstorm)

# django-sandstorm
Django package for helping integrate a django app with sandstorm.io

To use:
`pip install django-sandstorm`

It is HIGHLY recommended you make a separate sandstorm settings file for your
app. Whether or not you do, the following needs to go in your app settings for
integration with sandstorm to work:

```
INSTALLED_APPS += (
    'django_sandstorm',
)

MIDDLEWARE_CLASSES += (
    'django_sandstorm.middleware.SandstormMiddleware',
)

AUTH_USER_MODEL = "django_sandstorm.User"
```
