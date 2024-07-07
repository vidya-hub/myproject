from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from myapp.models import Department, Employee, Project, WorksOn



def employees(request):
    employees = Employee.objects.all()
    project_list = []
    len_e = len(employees)
    for it in range(len(employees)):
        temp1 = employees[it].project.all()
        for items3 in temp1:
            project_list.append((items3.name, employees[it].number))
    print(len(employees))
    return render(request, 'employees.html', {
        'employees': employees,
        'len': len_e,
        'project_list': project_list,
    })


def departments(request):
    return render(request, 'departments.html', {
        'departments': Department.objects.all(),
    })

def projects(request):
    return render(request, 'projects.html', {
        'projects': Project.objects.all(),
    })


def employeedetail(request, query):
    employee = Employee.objects.filter(number=query).get()
    project_list = employee.project.all()
    return render(request, 'employeedetail.html', {
        'employee': employee,
        'project_list': project_list,
    })


def departmentdetail(request, query):
    department = Department.objects.filter(number=query).get()
    employee_count = Employee.objects.filter(department_id=query).count()
    return render(request, 'departmentdetail.html', {
        'department': department,
        'employee_count': employee_count,
    })

def projectdetail(request, query):
        project = Project.objects.filter(number=query).get()
        employee_count = Employee.objects.filter(project__pk=query).count()
        return render(request, 'projectdetail.html', {
            'project': project,
            'employee_count': employee_count,
        })