"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from django.contrib import admin
from myapp import views

admin.autodiscover()

urlpatterns = [
    path('', views.employees, name='employees'),
    path('employees/', views.employees, name='employees'),
    path('departments/', views.departments, name='departments'),
    path('projects/', views.projects, name='projects'),
    re_path(r'^employee/(?P<query>\w+)/$', views.employeedetail),
    re_path(r'^department/(?P<query>\w+)/$', views.departmentdetail),
    re_path(r'^project/(?P<query>\w+)/$', views.projectdetail),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
]
