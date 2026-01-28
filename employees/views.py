from django.shortcuts import render,get_object_or_404,redirect
from employees.models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required

@login_required
def add_employee(request):
    form = EmployeeForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'add_employee.html', {'form': form})

@login_required
def update_employee(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST or None, request.FILES or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'update_employee.html', {'form': form})

@login_required
def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('home')

def employee_detail(request,pk):
   employee = get_object_or_404(Employee,pk=pk)
   context = {
      'employee': employee,
   }
   return render(request,'employee_detail.html',context)

