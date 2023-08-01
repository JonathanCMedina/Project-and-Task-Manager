from django.shortcuts import render, redirect
from accounts.forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
# this is for users to sign up and create an account
# linked to signup.html, url is "signup/" with name="signup"
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]

            if password == password_confirmation:
                user = User.objects.create_user(username, password=password)
                login(request, user)
                return redirect("projects_list")
            else:
                form.add_error("password", "The passwords do not match")
    else:
        form = SignUpForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


# this is for logging in
# html page is login.html, url is "login/" name="login"
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


# this is for logging out
# there is no html path because this is just a function that does something
# it does have a url path at "logout/" name="logout"
@login_required
def user_logout(request):
    logout(request)
    return redirect("login")
