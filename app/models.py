from django.db import models

# Create your models here.
class student(models.Model):
    sid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    age = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return (self.fname)