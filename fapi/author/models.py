from django.db import models
from django.contrib.auth.models import AbstractUser

class Author(AbstractUser):
    bio = models.TextField(max_length=500, default="Inset you descrpition here")
    age = models.IntegerField(default=18)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


