from response.views import (
    basic_response,
    api_response,
    html_fetcher,
    redicrector,
    file_handler,
    temp_response,
    page_not_found,
    bad_request,
    page_not_allowed,
    resp1,
    resp_status,
    SampleView,
    page_internal_error,
)
from django.urls import path

urlpatterns = [
    path("basic", basic_response),
    path("api", api_response),
    path("html", html_fetcher),
    path("redirect", redicrector),
    path("temp", temp_response),
    path("file", file_handler),
    path("not_found", page_not_found),
    path("internal_error", page_internal_error),
    path("bad", bad_request),
    path("not_allowed", page_not_allowed),
    path("drf1", resp1),
    path("drf_status", resp_status),
    path("class_view", SampleView.as_view()),
]
