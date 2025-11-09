from django.db import models

class Contact(models.Model):
    ism = models.CharField(max_length=50)
    telefon = models.CharField(max_length=20)
    email = models.EmailField()
    tugilgan_sana = models.DateField()
    qiziqishlar = models.TextField()