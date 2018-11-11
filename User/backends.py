from .models import User


class UsernameBackends:
    @staticmethod
    def authenticate(request, **credentials):
        username = credentials.get('username', credentials.get('username'))
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            pass
        else:
            if user.check_password(credentials['password']):
                return user

    @staticmethod
    def get_user(user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
