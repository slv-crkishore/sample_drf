from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from application.models import UserModel
from application.serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.generics import RetrieveUpdateDestroyAPIView
# Create your views here.


# class LoginApiView(TokenObtainPairView):
#     authentication_classes = [JWTAuthentication]

#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)

#         # queryset = UserModel.objects.all()
#         if user is not None:
#             serializer = TokenObtainPairSerializer(user)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(serializer.errors)

from rest_framework_simplejwt.views import TokenObtainPairView


class LoginApiView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        # breakpoint()

        if user is not None:
            refresh = RefreshToken.for_user(user)
            resp = {
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            }
            return Response(resp)


class CheckView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(request, *args, **kwargs):
        return Response("message: logged in and token verified")


class UserRegistrationView(ModelViewSet):
    permission_classes = [AllowAny]
    http_method_names = ['post']
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    # def post(self, request, *args, **kwargs):
    #     # queryset = UserModel.objects.all()
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.validated_data, status=status.HTTP_200_OK)

    #     return Response(serializer.errors)

    # def get(self, request):
    #     queryset = UserModel.objects.all()
    #     serializer = self.serializer_class(queryset, many=True)

    #     return Response(serializer.data)


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'patch', 'delete']
