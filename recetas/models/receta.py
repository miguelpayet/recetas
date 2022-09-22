from django.db import models
from random import *


class Receta(models.Model):
    actualizacion = models.DateTimeField(blank=True, null=True)
    consejos = models.CharField(max_length=2048, blank=True, null=True)
    creacion = models.DateTimeField(blank=True, null=True)
    descripcion = models.TextField(max_length=512, blank=True, null=True)
    dificultad = models.ForeignKey('Dificultad', blank=True, on_delete=models.CASCADE, null=True, db_column='iddificultad')
    idreceta = models.AutoField(primary_key=True)
    instrucciones = models.TextField(max_length=4096, blank=True, null=True)
    nombre = models.CharField(max_length=145, blank=True, null=True)
    origen = models.IntegerField(blank=True, null=True)
    porciones = models.IntegerField(blank=True, null=True)
    prioridad = models.IntegerField(blank=True, null=True)
    tipo = models.ForeignKey('Tipo', blank=True, on_delete=models.CASCADE, null=True, db_column='idtipo')
    visible = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    @classmethod
    def obtener_random(cls):
        recetas = Receta.objects.filter(visible=True)
        total = recetas.count()
        posicion = randint(1, total)
        return recetas[posicion - 1]

    class Meta:
        managed = False
        db_table = 'receta'
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
