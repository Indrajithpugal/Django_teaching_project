from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def basic_response(request):
    return HttpResponse(f"This is basic django HttpResponse {34 + 89}")


def api_response(request):
    return JsonResponse(
        {"name": "user", "email": "test@sample.com", "phone number": 224235}
    )


def html_fetcher(request):
    return render(request, "index.html")
