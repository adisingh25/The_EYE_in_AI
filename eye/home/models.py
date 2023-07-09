from django.db import models

# Create your models here.

class Feedback(models.Model):
    name100 = models.CharField(max_length=40)
    phonenumber100 = models.CharField(max_length=10)
    email100 = models.CharField(max_length=40)
    feedback100=models.TextField()

    def __str__(self):
        return self.name100
    
class Signup(models.Model):
    name20 = models.CharField(max_length=40)
    username20 = models.CharField(max_length=40)
    password20 = models.CharField(max_length=50)
    phonenumber20 = models.CharField(max_length=10)
    email20 = models.CharField(max_length=40)
    name30 = models.CharField(max_length=40)
    phonenumber30 = models.CharField(max_length=10)
    name40 = models.CharField(max_length=40)
    phonenumber40 = models.CharField(max_length=10)

    def __str__(self):
        return self.name20

