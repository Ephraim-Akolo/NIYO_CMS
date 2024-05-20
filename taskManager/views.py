from rest_framework import generics, permissions, exceptions
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
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
    
    def post(self, request, *args, **kwargs):
        resp = super().post(request, *args, **kwargs)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "tasks",
            {
                "type": "task_update",
                "message": {
                    "method": self.request.method,
                    **resp.data
                },
            }
            )
        return resp
    

class RetrieveUpdateDestroyTaskView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.UpdateTaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user        
        return Task.objects.filter(user=user)
    
    def put(self, request, *args, **kwargs):
        resp = super().put(request, *args, **kwargs)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "tasks",
            {
                "type": "task_update",
                "message": {
                    "method": self.request.method,
                    **resp.data
                },
            }
            )
        return resp
    
    def patch(self, request, *args, **kwargs):
        resp = super().patch(request, *args, **kwargs)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "tasks",
            {
                "type": "task_update",
                "message": {
                    "method": self.request.method,
                    **resp.data
                },
            }
            )
        return resp
    
    def delete(self, request, *args, **kwargs):
        resp = super().delete(request, *args, **kwargs)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "tasks",
            {
                "type": "task_update",
                "message": {
                    "method": self.request.method,
                    "id": kwargs['id']
                },
            }
            )
        return resp