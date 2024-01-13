from django.http import JsonResponse
from django.db.models import Sum
from .models import Task
from .serializers import SpaTaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  viewsets


# Creating a ViewSet for basic CRUD operations.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = SpaTaskSerializer

    # Defining partial_update to allow users to patch tasks, users can patch either the name, description, estimate or state.
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

# function that returns tasks categorized by state
@api_view(['GET'])
def task_list(request):

    pending_tasks = Task.objects.filter(state='PENDING')
    in_progress_tasks = Task.objects.filter(state='IN_PROGRESS')
    completed_tasks = Task.objects.filter(state='COMPLETED')

    pending_tasks_serializer = SpaTaskSerializer(pending_tasks, many=True)
    in_progress_tasks_serializer = SpaTaskSerializer(in_progress_tasks, many=True)
    completed_tasks_serializer = SpaTaskSerializer(completed_tasks, many=True)

    result = {
        'pending_tasks': pending_tasks_serializer.data,
        'in_progress_tasks': in_progress_tasks_serializer.data,
        'completed_tasks': completed_tasks_serializer.data,
    }

    return JsonResponse(result)

# Function that returns the sum of estimate categorized by status
@api_view(['GET'])
def sum_of_estimates_by_status(request):
    # Queries to calculate the sum of estimates for each state
    pending_sum = Task.objects.filter(state='PENDING').aggregate(Sum('estimate'))['estimate__sum'] or 0
    in_progress_sum = Task.objects.filter(state='IN_PROGRESS').aggregate(Sum('estimate'))['estimate__sum'] or 0
    completed_sum = Task.objects.filter(state='COMPLETED').aggregate(Sum('estimate'))['estimate__sum'] or 0

    response_data = {
        'pending_sum': pending_sum,
        'in_progress_sum': in_progress_sum,
        'completed_sum': completed_sum
    }

    return Response(response_data)