from django.db import models

# Create your models here.

class Enquiry(models.Model):
    name = models.CharField(max_length=50 ,blank=True, null=True)
    email = models.EmailField()
    subject = models.TextField(max_length=30 ,blank=True, null=True)
    message = models.TextField(max_length=50, blank=True, null=True)


class Blog(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=500 ,null=True,blank=True)
    date = models.DateField()
    description = models.CharField(max_length=500 ,blank=True, null=True)


