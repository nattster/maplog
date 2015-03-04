from django.db import models

# Create your models here.
class Location(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    color = models.CharField(max_length=6)
    added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)

    def __unicode__(self):
    	return self.title