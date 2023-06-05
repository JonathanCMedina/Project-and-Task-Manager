from accounts.views import signup, user_login, user_logout
from django.urls import path

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout")
]
