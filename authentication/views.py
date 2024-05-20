from rest_framework import generics
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import serializers


class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.CreateUserSerializer

    def post(self, request, *args, **kwargs):
        '''
        Create a user account on the platform if it does not exist.
        '''
        return super().post(request, *args, **kwargs)

