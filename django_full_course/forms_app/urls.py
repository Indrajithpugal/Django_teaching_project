from django.urls import path
from .views import employee_input, employee_post, display_employee

urlpatterns = [
    path("input", employee_input),
    path("employee_post", employee_post, name="success"),
    path("details", display_employee),
]
