from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    steps = models.CharField(max_length=20)
    image = models.FilePathField(default='',path="recipe/static/images")

    def __str__(name):
        return f"{name.title}"
