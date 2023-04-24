from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20)
    correo_electronico = models.EmailField()

    def __str__(self):
        return f'registrado {self.user.username}'
  
