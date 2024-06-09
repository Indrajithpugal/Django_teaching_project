from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def signup_view(request):
    """
    UserCreationForm: A built-in form provided by Django for creating a new user.
    CustomUserCreationForm: A custom form for creating a user. It should be defined in forms.py and inherit from UserCreationForm.
    The view handles both GET and POST requests. On POST, it processes the form data to create a new user.
    After a successful signup, the user is logged in automatically, and then redirected to the home page.
    """
    if request.method == "POST":

        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("form is valid")
            user = form.save()
            login(request, user)  # Log in the user after successful signup
            return redirect(
                "home"
            )  # Redirect to the home page or another appropriate page
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})


@csrf_exempt
def login_view(request):
    """
    AuthenticationForm: A built-in form provided by Django for authenticating a user.
    The view handles both GET and POST requests. On POST, it processes the form data to authenticate the user.
    After successful authentication, the user is logged in, and then redirected to the home page.
    """

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(
                "home"
            )  # Redirect to the home page or another appropriate page
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


@csrf_exempt
def logout_view(request):
    """
    The logout function provided by Django logs out the user.
    After logging out, the user is redirected to the home page.
    """

    logout(request)
    return redirect("home")  # Redirect to the home page or another appropriate page


def home_view(request):
    return render(request, "home.html")
