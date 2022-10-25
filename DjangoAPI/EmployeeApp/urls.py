from django.urls import path
from EmployeeApp.views import departmentApi, departmentDetailsApi

urlpatterns = [
    path('departments/', departmentApi),
    path('departments/<str:pk>/', departmentDetailsApi),
]