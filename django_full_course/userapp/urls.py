from django.urls import path
from .views import signup_view, login_view, logout_view, home_view, token_view

# from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("home/", home_view, name="home"),
    path("token/", token_view, name="token"),
]
