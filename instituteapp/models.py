from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CoursesData(models.Model):
    course_name = models.CharField(max_length=50)
    duration = models.CharField(max_length=40)
    fee = models.IntegerField()
    start_date = models.DateField()
    timings = models.TimeField()
    trainer_name = models.CharField(max_length=50)
    trainer_exp = models.CharField(max_length=50)
    training_mode = models.CharField(max_length=50)



class ContactData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length= 50)
    mobile = models.BigIntegerField()
    location = models.CharField(max_length=50)
    courses = models.CharField(max_length=50)
    referred_by = models.CharField(max_length=50)

class CommentData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length = 200)
   