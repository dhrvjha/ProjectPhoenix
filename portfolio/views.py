from typing import Any, Dict

from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from accounts.models import Account


class Home(View):
    """Home view for {ALLOWED_HOST}"""

    # TODO: design home.html
    template_name = "portfolio/home.html"

    def get(self, request):
        return render(request, self.template_name)


class UserPortfolioView(View):
    # TODO: create index.html and 404_error.html
    """Portfolio of a logged in user

    @info: Only logged in user can access this view
    """

    template_name = "portfolio/index.html"
    not_found_template_name = "portfolio/404_error.html"
    model = Account

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.request: HttpRequest
        self.username: str

    def get_queryset(self) -> Account:
        return self.model.objects.select_related("portfolio", "designtemplates").get(
            username=self.username
        )

    def get_context_data(self, **kwargs) -> Dict:
        context = {}
        try:
            queryset = self.get_queryset()
        except self.model.DoesNotExist:
            return None
        context["title"] = str(queryset)
        context["first_name"] = queryset.first_name
        context["last_name"] = queryset.last_name
        context["email"] = queryset.email
        context["username"] = queryset.username
        context["profile_picture"] = queryset.profile_picture
        context["css_reference"] = queryset.portfolio.designtemplates.css_reference_link
        return context

    def get(self, request, username):
        self.request = request
        self.username = username
        context = self.get_context_data()
        if context is not None:
            return render(request, self.template_name, context)
        http_page = render(request, self.not_found_template_name, context)
        http_page.status_code = 404
        return http_page
