from django.shortcuts import render
from .forms import EmployeeForm, EmployeeModelForm

# Create your views here.


def employee_input(request):
    form = EmployeeForm()
    return render(request, "employee_form.html", {"form": form})
