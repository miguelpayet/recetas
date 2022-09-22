from django.db import models


class Tipo(models.Model):
    idtipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'tipo'
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
