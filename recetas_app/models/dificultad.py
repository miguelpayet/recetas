from django.db import models


class Dificultad(models.Model):
    iddificultad = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'dificultad'
        verbose_name = 'Dificultad'
        verbose_name_plural = 'Dificultades'
