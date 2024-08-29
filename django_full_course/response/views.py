from django.shortcuts import render, redirect
from django.http import (
    HttpResponse,
    JsonResponse,
    FileResponse,
    HttpResponseBadRequest,
    HttpResponseNotAllowed,
    HttpResponseNotFound,
    HttpResponseServerError,
)
from django.template.response import TemplateResponse
import datetime
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication


# Create your views here.
# @permission_classes([IsAuthenticated])
def basic_response(request):
    """
    HttpResponse allows us to create an HttpResponse object with the content which we want to send as the
    response. as well as it will allow us to set HTTP headers, status codes as needed
    """
    response = HttpResponse(f"This is basic django HttpResponse {34 + 89}")
    response.status_code = 201
    response["creater"] = "pugal"
    return response


def api_response(request):
    """
    to create a json object and send it as response
    """

    return JsonResponse(
        {"name": "user", "email": "test@sample.com", "phone number": 224235}
    )


def html_fetcher(request):
    """
    render function to return html templates as responses. it is actually loading template and redering context  streamline the
    HttpResponse
    """
    return render(request, "index.html")


def redicrector(request):
    """
    to redirect the user into another url
    """
    return redirect("https://en.wikipedia.org/wiki/Django_(web_framework)")


def temp_response(request):
    """
    template response actually process the response before actually we render the template
    """
    now = datetime.datetime.now()
    time_dict = {"year": now.year, "month": now.month, "day": now.day, "hour": now.hour}
    return TemplateResponse(request, "time.html", context=time_dict)
    # return render(request, "time.html", context=time_dict)


def file_handler(request):
    """
    used to serve the files  as HTTP responses
    """
    file_path = "C:/User_Desk/Teaching_contents/Django_teaching_documents/Django_Full_Course_project/django_full_course/shiva_1.jpg"

    response = FileResponse(open(file_path, "rb"))

    # response["Content-Type"] = "application/jpg"  #this one causes for downloading the file when access request
    response["Content-Type"] = "image/jpg"  # to display image into the browser
    # response["Content-Disposition"] = 'attachement; filename = "sample.jpg"'
    return response


def page_internal_error(request):
    return HttpResponseServerError("server busy")


def bad_request(request):
    return HttpResponseBadRequest("seems like its a bad request")


def page_not_found(request):
    return HttpResponseNotFound("you are not allowed to view this page")


def page_not_allowed(request):
    return HttpResponseNotAllowed("this request not allowed from django")


@api_view(["GET"])
def resp1(request):
    return Response({"data": "get method received"})


@api_view(["GET", "POST"])
# @permission_classes([IsAuthenticated])
def resp_status(request):
    if request.method == "POST":
        return Response(
            {
                "request_status": "successful",
                "data": "post request processed successfully",
                "error_code": 0000,
            },
            status=status.HTTP_201_CREATED,
        )
    else:
        return Response(
            {
                "request_status": "successful",
                "data": "get request processed successfully",
                "error_code": 0000,
            },
            status=status.HTTP_202_ACCEPTED,
        )


from .serializers import ProductSerializer
from .models import Product


class SampleView(APIView):

    def get(self, request):
        data = Product.objects.all()
        # Pass 'many=True' to serialize a queryset
        response = ProductSerializer(data, many=True).data
        return Response({"data": response})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Product created successfully", "data": serializer.data}
            )
        return Response(serializer.errors, status=400)
