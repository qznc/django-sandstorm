from django.contrib.auth.middleware import AuthenticationMiddleware
from django.contrib.auth.models import User

from six.moves.urllib.parse import unquote

class SandstormMiddleware(AuthenticationMiddleware):
    def process_request(self, request):
        super(SandstormMiddleware, self).process_request(request)

        if request.META.get('HTTP_X_SANDSTORM_USERNAME') and hasattr(request, 'user'):
            request.user.sandstorm_id = unquote(
                request.META.get('HTTP_X_SANDSTORM_USERNAME')
            )
            if request.user.is_authenticated():
                request.user.save()
