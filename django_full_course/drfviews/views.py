from django.shortcuts import render
from admin_ui.models import Laptop
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    ListCreateAPIView,
)
from .serializers import LaptopSerializer

# Create your views here.


class LaptopView(ListAPIView):
    """
    uses the defined serializer to list out all the models objects  apis
    """

    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer


class LaptopCreate(CreateAPIView):
    """
    uses our serializer to handle the creation of objects
    """

    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer


class LaptopFetch(RetrieveAPIView):
    """
    used to fetch specific record based on passed id
    """

    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer


class LaptopUpdate(UpdateAPIView):
    """
    uses the defined serializer to update a single object
    """

    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer


class LaptopApi(ListCreateAPIView):
    """
    uses the defined serializer to list out all the models objects  apis
    """

    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
