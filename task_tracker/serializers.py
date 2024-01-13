from rest_framework import serializers
from .models import Task

class SpaTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'estimate', 'state']
        read_only_fields = ['id']