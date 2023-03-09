from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from application.views import LoginApiView, UserRegistrationView, CheckView, UserView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("register", UserRegistrationView, basename="registration")
router.register('register-details', UserView,
                basename="get or update user details")

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("login/", LoginApiView.as_view(), name="login"),
    path('verify/', CheckView.as_view(), name='verify login'),
    # path('register/', UserRegistrationView.as_view(), name="registration")
]
