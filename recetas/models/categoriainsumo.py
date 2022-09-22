from django.db import models


class CategoriaInsumo(models.Model):
    idcategoriainsumo = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    orden = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'categoriainsumo'
        verbose_name = 'Categoría de Insumo'
        verbose_name_plural = 'Categorías de Insumo'
