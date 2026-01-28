from django.shortcuts import render
from employees.models import Employee

def home(request):
    query = request.GET.get('q')
    employees = Employee.objects.all()
    if query:
        employees = employees.filter(
            first_name__icontains=query
        ) | employees.filter(
            last_name__icontains=query
        ) | employees.filter(
            designation__icontains=query
        )
    context = {
        'employees': employees,
        'query': query,
    }
    return render(request,'home.html',context)