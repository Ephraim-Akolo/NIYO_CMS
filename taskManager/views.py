from rest_framework import generics, permissions, exceptions
from . import serializers
from .models import Task


class ListCreateTaskView(generics.ListCreateAPIView):
    serializer_class = serializers.ListCreateTaskSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        user = self.request.user
        completed = self.request.GET.get('completed', None)
        if completed is not None:
            completed = str(completed).lower()
            if completed not in ("true", 'false'):
                raise exceptions.ValidationError("query parameter 'completed' must be 'true' or 'false'!")
            if completed == 'true':
                return Task.objects.filter(user=user, completed=True).order_by('-created')
            else:
                return Task.objects.filter(user=user, completed=False).order_by('-created')    
        return Task.objects.filter(user=user).order_by('-created')
    

class RetrieveUpdateDestroyTaskView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.UpdateTaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user        
        return Task.objects.filter(user=user)