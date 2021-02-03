from django.db import models

# Create your models here.


class blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    article = models.TextField(blank=True)
    url = models.URLField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title
