from . serializers import EmployeeSerializers
from rest_framework.viewsets import ModelViewSet
from . models import Employee
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EmployeeViewSet(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class= EmployeeSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]