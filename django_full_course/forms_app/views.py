from django.shortcuts import render
from .forms import EmployeeForm, EmployeeModelForm
from django.http import HttpResponse
from .models import Employee

# Create your views here.


def employee_input(request):
    form = EmployeeForm()
    return render(request, "form.html", {"form": form})


def employee_post(request):
    if request.method == "POST":
        form = EmployeeModelForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            address = form.cleaned_data["address"]
            print("name", name, "address", address)
            form.save()
            return HttpResponse("data posted successfully")


def display_employee(request):
    emp_data = Employee.objects.all()

    return render(request, "emp_details.html", {"employees": emp_data})
