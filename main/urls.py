
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#swagger configuration
schema_view = get_schema_view(
    openapi.Info(
        title = 'Task Management API',
        default_version = 'v1',
        description = 'API for task management',
        contact = openapi.Contact(email = 'udexter324@gmail.com')
    ),
    public = True,
    permission_classes = (permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('core.api.urls'), name = 'api'),

    #swagger documentation URL
    path('swagger/',schema_view.with_ui('swagger',cache_timeout = 0),name = 'schema-swagger-ui'),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout = 0), name = 'schema-redoc'),
]
