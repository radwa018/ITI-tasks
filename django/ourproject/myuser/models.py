from django.db import models

# Create your models here.

# class Track(models.Model):
#     id=models.AutoField(primary_key=True)
#     name=models.models.CharField(max_length=50,null=False)
from django.db import models

class Track(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Trainee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name="trainees")

    def __str__(self):
        return self.name
