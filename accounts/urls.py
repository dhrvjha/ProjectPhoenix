from django.contrib.auth import views
from django.urls import path

from accounts.views import RegisterAccount

urlpatterns = [
    path(
        "login/",
        views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("register/", RegisterAccount.as_view(), name="register"),
    path(
        "logout/",
        views.LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout",
    ),
]
