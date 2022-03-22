from django.db import models


class Visita(models.Model):
    request = models.CharField(max_length=1000, blank=True, null=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    idvisita = models.AutoField(primary_key=True)
    duracion = models.IntegerField(blank=True, null=True)
    protocol = models.CharField(max_length=10, blank=True, null=True)
    useragent = models.CharField(max_length=200, blank=True, null=True)
    platform = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visita'
