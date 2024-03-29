from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'estimate', 'state']
        # Defining id as read_only so that it cant be edited by users
        read_only_fields = ['id']