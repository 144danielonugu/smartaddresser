from django.db import models

# Create your models here.
class address(models.Model):
    fellowship=models.CharField(max_length=100)
    decription=models.CharField(max_length=100)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
class Note(models.Model):
    notename=models.CharField(max_length=100)
    note=models.TextField()
    dateposted=models.DateTimeField(auto_now_add=True)


