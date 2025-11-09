from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    message = models.TextField()
