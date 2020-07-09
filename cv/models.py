from django.db import models
from django.conf import settings

class Qualification(models.Model):
    title = models.CharField(max_length=200)
    awarding_body = models.CharField(max_length=200)
    text = models.TextField()
    date_started = models.DateField(blank=True, null=False)
    date_completed = models.DateField(null=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title