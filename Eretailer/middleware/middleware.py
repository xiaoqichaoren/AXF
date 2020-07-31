from django.utils.deprecation import MiddlewareMixin

from App.models import User
from App.utils import CHECK_PATH


class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path in CHECK_PATH:
            user_id = request.session.get('user_id')
            if user_id:
                users = User.objects.filter(pk=user_id)
                if users.exists():
                    request.user = users[0]
                    request.is_login = True
            else:
                request.is_login = False
