from django.urls import path
from .views import function1, function2

urlpatterns = [path("fun1", function1), path("fun2", function2)]
