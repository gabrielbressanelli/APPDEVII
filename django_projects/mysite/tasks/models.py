#from django.db import models

#class User(models.Model):
 #   username = models.CharField(max_length=255)
    # Add other user-related fields as needed

#class Schedule(models.Model):
 #   user = models.ForeignKey(User, on_delete=models.CASCADE)
  #  title = models.CharField(max_length=255)
   # description = models.TextField()
    #date = models.DateField()
    #time = models.TimeField()
    # Add other schedule-related fields as needed

from django.db import models
from django.contrib.auth.models import User

class Schedule(models.Model):
    # Your other fields
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    # ForeignKey to User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title