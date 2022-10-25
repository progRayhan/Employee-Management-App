from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def departmentApi(request):
    if request.method == 'GET':
        departments = Departments.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def departmentDetailsApi(request, pk):
    if request.method == 'GET':
        department = Departments.objects.get(pk=pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    if request.method == 'PUT':
        department = Departments.objects.get(pk=pk)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        department = Departments.objects.get(pk=pk)
        department.delete()
        return Response({'Content just deleted'})