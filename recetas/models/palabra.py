from django.db import models


class Palabra(models.Model):
    idpalabra = models.AutoField(primary_key=True)
    palabra = models.CharField(unique=True, max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=11, blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'palabra'
        
