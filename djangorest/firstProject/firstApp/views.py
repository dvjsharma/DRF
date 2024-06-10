from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee

# Create your views here.
def employeeView(request):
    data = Employee.objects.all()
    response = {"employees": list(data.values("name", "salary"))}
    return JsonResponse(response) #JsonResponse is a serializer here
