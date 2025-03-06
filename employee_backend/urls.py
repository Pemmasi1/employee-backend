# filepath: /Users/sivanjaneyulupemmasani/python/employee-backend/employee_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

API_TITLE = 'Employee API'
API_DESCRIPTION = 'A Web API for managing employees and departments.'
schema_view = get_schema_view(
    openapi.Info(
        title=API_TITLE,
        default_version='v1',
        description=API_DESCRIPTION,
    ),
    public=True,
    permission_classes=(),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('employee.urls')),
    path('api/', include('department.urls')),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]