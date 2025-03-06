from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

API_TITLE = 'Employee API'
API_DESCRIPTION = 'A Web API for managing employees and departments.'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employee/', include('employee.urls')),
    path('api/department/', include('department.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]