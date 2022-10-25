from django.urls import path
from EmployeeApp.views import departmentApi, departmentDetailsApi, employeeApi, employeeDetailsApi

urlpatterns = [
    path('departments/', departmentApi),
    path('departments/<str:pk>/', departmentDetailsApi),

    path('employees/', employeeApi),
    path('employees/<str:pk>/', employeeDetailsApi),
]