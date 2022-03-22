from django.db import models


class Receta(models.Model):
    idreceta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=145, blank=True, null=True)
    descripcion = models.CharField(max_length=512, blank=True, null=True)
    porciones = models.IntegerField(blank=True, null=True)
    instrucciones = models.CharField(max_length=4096, blank=True, null=True)
    consejos = models.CharField(max_length=2048, blank=True, null=True)
    idtipo = models.IntegerField(blank=True, null=True)
    creacion = models.DateTimeField(blank=True, null=True)
    actualizacion = models.DateTimeField(blank=True, null=True)
    iddificultad = models.IntegerField(blank=True, null=True)
    visible = models.IntegerField(blank=True, null=True)
    origen = models.IntegerField(blank=True, null=True)
    prioridad = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'receta'
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
