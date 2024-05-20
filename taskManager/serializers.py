from rest_framework import serializers
from .models import Task


class ListCreateTaskSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user = serializers.SerializerMethodField()
    title = serializers.CharField()
    body = serializers.CharField()
    completed = serializers.BooleanField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)
    created = serializers.DateTimeField(read_only=True)

    class Meta(object):
        model = Task
        fields = ('id', 'user', 'title', 'body', 'completed', 'modified', 'created')

    def get_user(self, obj) -> serializers.EmailField:
        return obj.user.email


    def create(self, validated_data):
        title = validated_data.pop("title")
        body = validated_data.pop("body")
        user = self.context['request'].user
        task = Task.objects.create(user=user, title=title, body=body, completed=False)
        return task
    

class UpdateTaskSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user = serializers.SerializerMethodField()
    title = serializers.CharField()
    body = serializers.CharField()
    completed = serializers.BooleanField()
    modified = serializers.DateTimeField(read_only=True)
    created = serializers.DateTimeField(read_only=True)

    class Meta(object):
        model = Task
        fields = ('id', 'user', 'title', 'body', 'completed', 'modified', 'created')

    def get_user(self, obj) -> serializers.EmailField:
        return obj.user.email

    def update(self, task:Task, validated_data):
        title = validated_data.pop("title", None)
        body = validated_data.pop("body", None)
        completed = validated_data.pop("completed", None)
        if title:
            task.title = title
        if body:
            task.body = body
        if completed:
            task.completed = completed
        task.save()
        return task