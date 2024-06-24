from django.urls import path
from .views import LaptopView, LaptopCreate, LaptopFetch, LaptopUpdate, LaptopApi

urlpatterns = [
    path("genericlap", LaptopView.as_view()),
    path("laptopcreate", LaptopCreate.as_view()),
    path("laptopfetch/<int:pk>", LaptopFetch.as_view()),
    path("laptopupdate/<int:pk>", LaptopUpdate.as_view()),
    path("lap_get_post", LaptopApi.as_view()),
]
