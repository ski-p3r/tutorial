from djoser.serializers import UserCreateSerializer as BaseUser, UserSerializer as BaseSer

class UserCreateSerializer(BaseUser):
    class Meta(BaseUser.Meta):
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password']

class UserSerializer(BaseSer):
    class Meta(BaseSer.Meta):
        fields = ["id", "first_name", "last_name", "email", "username"]