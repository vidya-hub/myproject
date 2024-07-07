from django.contrib import admin


from django.contrib.auth.models import User
from myapp.models import Department, Employee,WorksOn,Project

# Register your models here.


admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(WorksOn)
admin.site.register(Project)