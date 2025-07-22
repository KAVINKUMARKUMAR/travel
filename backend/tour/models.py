from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
