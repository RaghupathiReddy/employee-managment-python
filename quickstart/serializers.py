from quickstart.models import Project, Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(source='manager', read_only=True, many=True)
    class Meta:
        model = Employee
        fields = ('id', 'name', 'employees')


class ProjectSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(source='project', read_only=True, many=True)
    class Meta:
        model = Project
        fields = '__all__'