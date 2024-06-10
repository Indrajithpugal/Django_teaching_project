from response.views import basic_response, api_response, html_fetcher
from django.urls import path

urlpatterns = [
    path("basic", basic_response),
    path("api", api_response),
    path("html", html_fetcher),
]
