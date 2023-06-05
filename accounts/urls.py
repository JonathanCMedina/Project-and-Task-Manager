from accounts.views import signup, user_login
from django.urls import path

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", user_login, name="login")
]
