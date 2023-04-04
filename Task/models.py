from django.db import models

# Create your models here.


class Task(models.Model):
    tache_name=models.CharField(max_length=150)
    
    
    def __str__(self):
        return self.tache_name