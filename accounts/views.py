from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from accounts.forms import AccountRegisterForm
from accounts.models import Account
from portfolio.models import Portfolio


class RegisterAccount(View):
    template_name = "accounts/register.html"

    def __init__(self):
        super().__init__()
        self.request: HttpRequest

    def get_context_data(self):
        context = {"form": AccountRegisterForm(self.request.POST), "title": "Register"}
        return context

    def get(self, request):
        self.request = request
        return render(request, self.template_name, self.get_context_data())

    def post(self, request):
        self.request = request
        context = self.get_context_data()
        form = context.get("form")
        if form.is_valid():
            account = form.save()
            Portfolio(user=account).save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("login")
        else:
            messages.error(request, "Account not created! Try again later")
        return render(request, self.template_name, context)


class AccountSettings(View):
    template_name = "accounts/account.html"
    model = Account

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.request: HttpRequest

    def get_queryset(self):
        return self.model.objects.select_related("portfolio", "designtemplates").get(
            id=self.request.id
        )

    def get_context_data(self, **kwargs):
        context = {}
        queryset = self.get_queryset()
        context["title"] = f"{queryset}'s Profile"
        context["first_name"] = queryset.first_name
        context["last_name"] = queryset.last_name
        context["email"] = queryset.email
        context["username"] = queryset.username
        context["profile_picture"] = queryset.profile_picture
        context["css_reference"] = queryset.portfolio.designtemplates.css_reference_link
        return context

    def get(self, request):
        self.request = request
        context = self.get_context_data()
        return render(request, self.template_name, context)
