from django.db import models
from django.conf import settings

class Qualification(models.Model):
    title = models.CharField(max_length=200)
    awarding_body = models.CharField(max_length=200)
    text = models.TextField()
    date_started = models.DateField(blank=True, null=True)
    date_completed = models.DateField(null=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    date_started = models.CharField(max_length=50, null=False)
    date_completed = models.CharField(max_length=50, null=False)
    text = models.TextField()

    def __str__(self):
        return self.title

class Interest(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title