from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title=models.CharField(max_length=300)
    description=models.CharField(max_length=1000)
    pay=models.CharField(max_length=10)
    location=models.CharField(max_length=200)
    duration=models.CharField(max_length=50)
    application_date=models.DateField()
    application_deadline=models.DateField()
    def __str__(self):
        return self.title



    