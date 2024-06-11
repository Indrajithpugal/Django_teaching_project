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


# Create your views here.
def basic_response(request):
    return HttpResponse(f"This is basic django HttpResponse {34 + 89}")


def api_response(request):
    return JsonResponse(
        {"name": "user", "email": "test@sample.com", "phone number": 224235}
    )


def html_fetcher(request):
    return render(request, "index.html")


def redicrector(request):
    return redirect("https://en.wikipedia.org/wiki/Django_(web_framework)")


def temp_response(request):
    now = datetime.datetime.now()
    time_dict = {"year": now.year, "month": now.month, "day": now.day, "hour": now.hour}
    return TemplateResponse(request, "time.html", context=time_dict)


def file_handler(request):
    file_path = "C:/User_Desk/Teaching_contents/Django_teaching_documents/Django_Full_Course_project/django_full_course/shiva_1.jpg"

    response = FileResponse(open(file_path, "rb"))

    response["Content-Type"] = "application/jpg"
    response["Content-Disposition"] = 'attachement; filename = "sample.jpg"'
    return response


def page_not_found(request):
    return HttpResponseServerError("server busy")


def bad_request(request):
    return HttpResponseBadRequest("seems like its a bad request")


def page_not_allowed(request):
    return HttpResponseNotFound("you are not allowed to view this page")


def page_not_found(request):
    return HttpResponseServerError("server busy")
