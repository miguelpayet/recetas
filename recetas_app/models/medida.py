from django.db import models


class Medida(models.Model):
    idmedida = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=145, blank=True, null=True)
    plural = models.CharField(max_length=3, blank=True, null=True)
    ocultar = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medida'

