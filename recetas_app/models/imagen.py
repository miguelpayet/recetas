from django.db import models


class Imagen(models.Model):
    idimagen = models.AutoField(primary_key=True)
    idreceta = models.ForeignKey('Receta', models.DO_NOTHING, db_column='idreceta')
    ruta = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'imagen'
       