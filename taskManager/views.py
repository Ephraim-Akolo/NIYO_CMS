from rest_framework import generics, permissions, exceptions
from . import serializers
from .models import Task


class ListCreateTaskView(generics.ListCreateAPIView):
    serializer_class = serializers.ListCreateTaskSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        user = self.request.user        
        return Task.objects.filter(user=user).order_by('-created')