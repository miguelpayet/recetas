from django.db import models


class Ingrediente(models.Model):
    idingrediente = models.AutoField(primary_key=True)
    idreceta = models.ForeignKey('Receta', models.DO_NOTHING, db_column='idreceta')
    idinsumo = models.ForeignKey('Insumo', models.DO_NOTHING, db_column='idinsumo')
    idmedida = models.ForeignKey('Medida', models.DO_NOTHING, db_column='idmedida')
    cantidad = models.FloatField(blank=True, null=True)
    indicaciones = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingrediente'
