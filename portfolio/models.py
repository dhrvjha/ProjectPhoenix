from django.contrib.auth import get_user_model
from django.db import models


class Portfolio(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name="portfolio"
    )
    css_reference_link = models.URLField(default="/static/css/style.css")
