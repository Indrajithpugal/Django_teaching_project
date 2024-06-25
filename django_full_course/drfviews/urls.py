from django.urls import path, include
from .views import (
    LaptopView,
    LaptopCreate,
    LaptopFetch,
    LaptopUpdate,
    LaptopApi,
    GroceryView,
    GroceryImageView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("grocery", GroceryView)
router.register("image", GroceryImageView, na)

urlpatterns = [
    path("genericlap", LaptopView.as_view()),
    path("laptopcreate", LaptopCreate.as_view()),
    path("laptopfetch/<int:pk>", LaptopFetch.as_view()),
    path("laptopupdate/<int:pk>", LaptopUpdate.as_view()),
    path("lap_get_post", LaptopApi.as_view()),
    path("viewset/", include(router.urls)),
]
