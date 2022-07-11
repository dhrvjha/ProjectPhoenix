
from designtemplates.models import DesignTemplate
from django.contrib.auth import get_user_model
from django.db import models


class Portfolio(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name="portfolio"
    )
    design = models.ForeignKey(
        DesignTemplate, on_delete=models.DO_NOTHING, related_name="designtemplates"
    )
