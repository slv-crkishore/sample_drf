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
from django.contrib.auth import authenticate
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


class LoginApiView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


# class CheckView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(request, *args, **kwargs):
#         return Response("message: logged in")

class UserRegistrationView(ModelViewSet):
    permission_classes = [AllowAny]
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
