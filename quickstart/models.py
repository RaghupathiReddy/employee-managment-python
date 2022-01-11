from django.db import models

# Create your models here.

class EmployeeManager(models.Manager):
    def get_queryset(self):
        return super(EmployeeManager, self).get_queryset().filter(is_manager=True)


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Employee(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=10)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name="project")
    manager_id = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="manager")
    salary = models.IntegerField(default=0)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    all_employees = models.Manager()
    managers = EmployeeManager()