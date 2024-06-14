from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import HousesDetails

# Create your views here.


@csrf_exempt
def function1(request):
    if request.method == "GET":
        data = HousesDetails.objects.all().values()
        return HttpResponse(data)
    elif request.method == "POST":
        # will convert bytes of the html payload into  python dictionary
        data = json.loads(request.body)
        HousesDetails.objects.create(
            no_of_bedrooms=data["no_of_bedrooms"],
            no_of_bathrooms=data["no_of_bathrooms"],
            sqrt_feets=data["sqrt_feets"],
            price=data["price"],
            desc=data["desc"],
        )
        return HttpResponse("data posted succesfully")
