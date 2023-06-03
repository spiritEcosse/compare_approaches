from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=30)
