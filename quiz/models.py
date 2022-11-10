from django.db import models

# Create your models here.


class Quiz(models.Model):
    question = models.CharField(max_length=1000, null=True, blank=True)
    answer = models.CharField(max_length=1000, null=True, blank=True)
    file = models.FileField(upload_to="files/", blank=True, null=True)
