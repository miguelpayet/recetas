from django.db import models


class Insumo(models.Model):
    idinsumo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    plural = models.CharField(max_length=145, blank=True, null=True)
    categoriainsumo = models.ForeignKey('CategoriaInsumo', on_delete=models.CASCADE, db_column='idcategoriainsumo',
                                        blank=True, null=True)
    descripcion = models.CharField(max_length=512, blank=True, null=True)

    def __lt__(self, other):
        return self.nombre < other.nombre

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'insumo'
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'
