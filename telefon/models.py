from django.db import models

# Create your models here.
class Phone(models.Model):
    nomi = models.CharField(max_length=255)
    narxi = models.IntegerField(default=0)
    haqida = models.TextField()
    
    def __str__(self):
        return f'{self.nomi}'