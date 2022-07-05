from django.shortcuts import render
from django.views import View


class Home(View):
    """Home view for {ALLOWED_HOST}"""

    template_name = "portfolio/home.html"

    def get(self, request):
        return render(request, self.template_name)
