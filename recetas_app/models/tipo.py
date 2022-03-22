from django.db import models


class Tipo(models.Model):
    idtipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo'
