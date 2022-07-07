from django.contrib.auth.decorators import login_required
from django.urls import path

from portfolio.views import Home, UserPortfolioView

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path(
        "<username:slug>/",
        login_required(UserPortfolioView.as_view()),
        name="portfolio_view",
    ),
]
