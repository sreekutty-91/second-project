from django.db import models

# Create your models here.
class Students(models.Model):
    Std_id = models.IntegerField()
    Name = models.CharField(max_length=225)
    Course = models.CharField(max_length=225)
    Email = models.EmailField()
