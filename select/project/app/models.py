from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    image=models.FileField(upload_to='image/')
    video=models.FileField(upload_to='viedeo/')
    audio=models.FileField(upload_to='audio/')



