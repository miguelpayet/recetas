from django.db import models

from recetas_app.models.receta import Receta
from recetas_app.models.categoria import Categoria


class RecetaCategoria(models.Model):
    idrecetacategoria = models.AutoField(primary_key=True)
    idreceta = models.ForeignKey(Receta, models.DO_NOTHING, db_column='idreceta')
    idcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='idcategoria')

    class Meta:
        managed = False
        db_table = 'receta_categoria'
        unique_together = (('idreceta', 'idcategoria'),)
