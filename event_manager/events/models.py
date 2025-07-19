from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    title= models.CharField(max_length=200)
    date= models.DateTimeField()
    location= models.CharField(max_length=255)
    description= models.TextField()
    image= models.ImageField(upload_to='event_images/')
    created_by= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
