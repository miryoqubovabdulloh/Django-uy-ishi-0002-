from django.db import models

# Create your models here.
class Moshina(models.Model):
    nomi = models.CharField(max_length=255)
    narxi = models.IntegerField(default=0)
    rangi = models.CharField(max_length=100)  
    haqida = models.TextField()
    
    def __str__(self):
        return f'{self.nomi}'