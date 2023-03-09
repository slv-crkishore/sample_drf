from rest_framework.serializers import ModelSerializer
from application.models import UserModel


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        exclude = ["password"]
