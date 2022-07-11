from django.shortcuts import render
from django.views import View

from designtemplates.models import DesignTemplate


class DesignAddView(View):
    pass


class DesignListView(View):
    # TODO: list_view.html
    template_name = "designtemplates/list_view.html"
    model = DesignTemplate

    def get_queryset(self) -> DesignTemplate:
        return self.model.objects.all().select_related("design_templates_screen_shots")

    def get_context_data(self, **kwargs):
        queryset = self.get_queryset()
        context = {}
        context["designs"] = [
            {
                "name": design.name,
                "css_reference": design.css_reference_link,
                "description": design.description,
                "pictures": [
                    urls for urls in design.design_templates_screen_shots.picture
                ],
            }
            for design in queryset
        ]
        return context

    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
