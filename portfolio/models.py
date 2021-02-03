from django.db import models

# Create your models here.


class project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
