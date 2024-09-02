from django.db import models

# Create your models here.

class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField(max_length=30)
    message = models.TextField(max_length=50)


class Blog(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=500)
    date = models.DateField()
    description = models.CharField(max_length=500)


