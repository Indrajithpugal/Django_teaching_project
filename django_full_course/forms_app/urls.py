from django.urls import path
from .views import employee_input

urlpatterns = [path("input", employee_input)]
