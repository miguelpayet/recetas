from django.db import models


class Medida(models.Model):
    idmedida = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=145, blank=True, null=True)
    plural = models.CharField(max_length=3, blank=True, null=True)
    ocultar = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'medida'
        verbose_name = 'Medida'
        verbose_name_plural = 'Medidas'
