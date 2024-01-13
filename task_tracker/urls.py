from django.contrib import admin
from django.urls import path
from .views import TaskViewSet
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', views.task_list),
    path('estimate-sum/', views.sum_of_estimates_by_status)
]

urlpatterns += router.urls