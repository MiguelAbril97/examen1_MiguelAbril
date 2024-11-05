from django.db import models
from django.utils import timezone

# Create your models here.

class Hamaca (models.Model):
    nombre = models.CharField(max_length=50)
    material = models.CharField(max_length=100)
    longitud =  models.FloatField(default=1.0)
    peso_maximo = models.FloatField(default=1.0)
    
class Usuario (models.Model):
    nombre = models.CharField(max_length=100)
    voto = models.ManyToManyField(Hamaca, through='Valoracion')
    
class Banco (models.Model):
    BANCOS = [
        ('BBVA', 'BBVA'),
        ('UNI','Unicaja'),
        ('CAI', 'Caixa'),
        ('ING','ING'),
    ]
    
    banco = models.CharField(
        max_length=4,
        choices=BANCOS
        )
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Valoracion (models.Model):
    hamaca = models.ForeignKey(Hamaca, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    valor = models.FloatField(default=1.0)
    comentario = models.CharField(max_length=200)
    fecha_valoracion = models.DateTimeField(default=timezone.now)