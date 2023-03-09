from rest_framework.serializers import ModelSerializer
from application.models import UserModel
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(ModelSerializer):

    class Meta:
        model = UserModel
        fields = "__all__"
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }
