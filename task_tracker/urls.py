from django.contrib import admin
from django.urls import path, include
from .views import TaskViewSet
from . import views
from rest_framework import routers, permissions
# For Auto-documentation with swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# OPENAPI schema
schema_view = get_schema_view(
    openapi.Info(
        title="REST APIs",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet, basename='task')

urlpatterns = [
    # Include DRF-Swagger URLs
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # API URLs
    path('admin/', admin.site.urls),
    path('tasks/', views.task_list),
    path('estimate-sum/', views.sum_of_estimates_by_status)
]

urlpatterns += router.urls