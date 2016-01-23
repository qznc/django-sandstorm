from django.contrib import auth
from django.contrib.auth.middleware import RemoteUserMiddleware
from django.contrib.auth.models import User

class SandstormMiddleware(RemoteUserMiddleware):
    """
    Requires 'django.contrib.auth.backends.RemoteUserBackend'in 
    settings.AUTHENTICATION_BACKENDS
    """

    header = 'X-Sandstorm-User-Id'

