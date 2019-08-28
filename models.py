from django.db import models

# Create your models here.
class Color(models.Model):
    hex = models.CharField(max_length=6)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name