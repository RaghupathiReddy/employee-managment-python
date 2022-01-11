from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import ProjectSerializer, EmployeeSerializer, ManagerSerializer
from quickstart.models import Project, Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.all_employees.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Employee.managers.all()
    serializer_class = ManagerSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]