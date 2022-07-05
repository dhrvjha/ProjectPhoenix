
from django.urls import path
from portfolio.views import Home

urlpatterns = [
    path("", Home.as_view(), name="home")
]
