from django.shortcuts import render, redirect, get_object_or_404
from .form import EmployeesForm
from .models import Employees

# Create your views here.

def home(request):
    if request.method=='POST':
        form=EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            form=EmployeesForm() 
    else:
        form=EmployeesForm()
    
    data=Employees.objects.all()
    
    context={
        'form':form,
        'data':data
    }

    
    return render(request, "home.html", context)

def edit(request, id):
    emp=get_object_or_404(Employees, id=id)

    if request.method=='POST':
        form=EmployeesForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form=EmployeesForm(instance=emp)

    data=Employees.objects.all()

    context={
        'form':form,
        'data':data
    }

    return render(request, 'home.html',context)


def delete(request, id):
    emp=get_object_or_404(Employees, id=id)
    emp.delete()
    return redirect('home')





