from .models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # Our model
        model = Task

        # Any fields we want to serialize
        fields = ['id', 'title', 'description', 'created_on', 'complete']