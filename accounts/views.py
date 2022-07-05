from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from accounts.forms import AccountRegisterForm


class RegisterAccount(View):
    template_name = "accounts/register.html"

    def __init__(self):
        super().__init__()
        self.request: HttpRequest

    def get_context_data(self):
        context = {
            "form": AccountRegisterForm(self.request.POST),
            "title": "Register"
        }
        return context

    def get(self, request):
        self.request = request
        return render(request, self.template_name, self.get_context_data())

    def post(self, request):
        self.request = request
        print("*"*25)
        print("\n\n")
        print(self.request.POST)
        print("\n\n")
        print("*"*25)
        context = self.get_context_data()
        form = context.get("form")
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("login")
        else:
            messages.error(request, "Account not created! Try again later")
        return render(request, self.template_name, context)
