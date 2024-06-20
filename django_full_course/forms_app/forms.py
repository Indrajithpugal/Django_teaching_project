from django import forms
from .models import Employee


class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=90)
    email = forms.EmailField()
    phone = forms.IntegerField()
    address = forms.CharField()


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
