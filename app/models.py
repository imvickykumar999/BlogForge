# myapp/models.py

from django.db import models

class Domaindata(models.Model):
    keyword = models.CharField(max_length=100)
    url1 = models.URLField(max_length=200)
    min_count = models.IntegerField(default=0)
    max_count = models.IntegerField()
    url2 = models.URLField(max_length=200)

    def __str__(self):
        return self.keyword
