from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from .models import HousesDetails
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@csrf_exempt
def function1(request):
    if request.method == "GET":  # to fetch the details
        data = HousesDetails.objects.all().values()
        return HttpResponse(data)

    elif request.method == "POST":  # receiving the payloads
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

    elif (
        request.method == "PUT"
    ):  # receive payload for updation  updating the entire record
        data = json.loads(request.body)
        instance = HousesDetails.objects.filter(id=data["id"]).first()
        instance.no_of_bedrooms = data.get("no_of_bedrooms", instance.no_of_bedrooms)
        instance.no_of_bathrooms = data.get("no_of_bathrooms", instance.no_of_bathrooms)
        instance.sqrt_feets = data.get("sqrt_feets", instance.sqrt_feets)
        instance.price = data.get("price", instance.price)
        instance.desc = data.get("desc", instance.desc)
        instance.save()
        return HttpResponse("data updated succesfully")

    elif request.method == "PATCH":  # updating specific part of the record

        data = json.loads(request.body)
        instance = HousesDetails.objects.filter(id=data["id"]).first()
        instance.no_of_bedrooms = data.get("no_of_bedrooms", instance.no_of_bedrooms)
        instance.save()
        return HttpResponse("data updated succesfully")

    elif request.method == "DELETE":  # filter the record and delete
        data = json.loads(request.body)
        instance = HousesDetails.objects.filter(id=data["id"]).first()
        instance.delete()
        return HttpResponse("data deleted succesfully")
    else:
        return HttpResponseBadRequest("no request method found")


@api_view(["GET", "POST", "PUT", "DELETE"])
def function2(request):

    if request.method == "GET":
        data = HousesDetails.objects.all().values()
        return Response(data)

    elif request.method == "POST":
        data = request.data
        HousesDetails.objects.create(
            no_of_bedrooms=data["no_of_bedrooms"],
            no_of_bathrooms=data["no_of_bathrooms"],
            sqrt_feets=data["sqrt_feets"],
            price=data["price"],
            desc=data["desc"],
        )
        return Response(
            {
                "status": True,
                "success": True,
                "message": "data posted successfully",
                "error code": 00000,
            },
            status=status.HTTP_201_CREATED,
        )

    elif request.method == "PUT":
        data = request.data
        instance = HousesDetails.objects.filter(id=data["id"]).first()
        instance.no_of_bedrooms = data.get("no_of_bedrooms", instance.no_of_bedrooms)
        instance.no_of_bathrooms = data.get("no_of_bathrooms", instance.no_of_bathrooms)
        instance.sqrt_feets = data.get("sqrt_feets", instance.sqrt_feets)
        instance.price = data.get("price", instance.price)
        instance.desc = data.get("desc", instance.desc)
        instance.save()

        return Response(
            {
                "status": True,
                "success": True,
                "message": "data updated successfully",
                "error code": 00000,
            },
            status=status.HTTP_205_RESET_CONTENT,
        )

    elif request.method == "DELETE":

        data = request.data
        instance = HousesDetails.objects.filter(id=data["id"]).first()
        instance.delete()

        return Response(
            {
                "status": True,
                "success": True,
                "message": "data deleted successfully",
                "error code": 00000,
            },
            status=status.HTTP_204_NO_CONTENT,
        )
