from django.db import models


class Ingrediente(models.Model):
    cantidad = models.FloatField(blank=True, null=True)
    idingrediente = models.AutoField(primary_key=True)
    indicaciones = models.CharField(max_length=512, blank=True, null=True)
    insumo = models.ForeignKey('Insumo', models.DO_NOTHING, db_column='idinsumo')
    medida = models.ForeignKey('Medida', models.DO_NOTHING, db_column='idmedida', to_field='idmedida')
    receta = models.ForeignKey('Receta', models.DO_NOTHING, db_column='idreceta', related_name='ingredientes')

    def descripcion(self):
        return f"{self.cantidad} {self.medida.nombre} de {self.insumo.nombre}"

    def __str__(self):
        return self.insumo.nombre

    class Meta:
        managed = False
        db_table = 'ingrediente'
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'
