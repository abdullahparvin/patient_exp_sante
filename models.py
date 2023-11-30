from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key="True")
    name = models.CharField(max_length=300)
    age = models.IntegerField()
    male = "m"
    female = "f"
    sex_choices = [(male, "male"), (female, "female")]
    sex = models.CharField(max_length=2, choices=sex_choices)
    location = models.CharField(max_length=300)
    health = models.CharField(max_length=300)

    def __str__(self):
         return f" You are '{self.name}', '{self.age}' years old and living in '{self.location}"

class Chats(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     message = models.CharField(max_length=500)

# Create your models here.
