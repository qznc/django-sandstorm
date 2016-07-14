from django.contrib.auth.middleware import AuthenticationMiddleware

from six.moves.urllib.parse import unquote

from .models import User

class SandstormMiddleware(AuthenticationMiddleware):
    def process_request(self, request):
        super(SandstormMiddleware, self).process_request(request)

        sid = request.META.get('HTTP_X_SANDSTORM_USER_ID')
        if sid:
            name = unquote(request.META.get('HTTP_X_SANDSTORM_USERNAME'))
            handle = unquote(request.META.get('HTTP_X_SANDSTORM_PREFERRED_HANDLE'))
            u = User(sandstorm_id=sid, name=name, handle=handle)
            try:
                u.save()
            except:
                pass
            if hasattr(request, 'user'):
                request.user = u
