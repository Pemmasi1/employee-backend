import logging
from rest_framework import viewsets
from .models import Department
from .serializers import DepartmentSerializer

logger = logging.getLogger(__name__)

class DepartmentViewSet(viewsets.ModelViewSet):
    logger.info('DepartmentViewSet')
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer