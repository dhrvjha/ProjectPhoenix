from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    about_me = models.TextField(blank=True, null=True, max_length=1000)
    profile_picture = models.URLField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Article(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    link = models.URLField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"
