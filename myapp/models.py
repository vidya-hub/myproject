from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name")
    number = models.CharField(max_length=255, blank=True, verbose_name="Number", primary_key=True)

    def __str__(self):
        return f"{self.name} - {self.number}"

class Project(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name")
    number = models.CharField(max_length=255, blank=True, verbose_name="Number", primary_key=True)

    def __str__(self):
        return f"{self.name} - {self.number}"

    def project_ids(self):
        return f"project_{self.id}"

class Employee(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name")
    number = models.CharField(max_length=255, blank=True, verbose_name="Number", primary_key=True)
    salary = models.CharField(max_length=255, blank=True, null=True, verbose_name="Salary")
    department = models.ForeignKey(Department, related_name="departmentname", blank=True, null=True, default=None, on_delete=models.CASCADE)
    project = models.ManyToManyField(Project, verbose_name="Project", through='WorksOn')

    def __str__(self):
        return f"{self.name} - {self.number} - {self.department.number}"

class WorksOn(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.name} - {self.project.name}"
