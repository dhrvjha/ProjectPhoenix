from django.contrib.auth import get_user_model
from django.db import models


class DesignTemplate(models.Model):
    """ Model which stores design file links for portfolio """
    css_reference_link = models.URLField(default="/static/css/style.css")
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)


class DesignTemplatesScreenShots(models.Model):
    """ Model which stores ss for Design Templates for portfolio"""
    design = models.ForeignKey(
        DesignTemplate,
        on_delete=models.CASCADE,
        related_name="design_templates_screen_shots",
    )
    picture = models.URLField()
