from django.db import models


class Ingrediente(models.Model):
    idingrediente = models.AutoField(primary_key=True)
    receta = models.ForeignKey('Receta', models.DO_NOTHING, db_column='idreceta')
    insumo = models.ForeignKey('Insumo', models.DO_NOTHING, db_column='idinsumo')
    medida = models.ForeignKey('Medida', models.DO_NOTHING, db_column='idmedida')
    cantidad = models.FloatField(blank=True, null=True)
    indicaciones = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.insumo.nombre

    class Meta:
        managed = False
        db_table = 'ingrediente'
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'
