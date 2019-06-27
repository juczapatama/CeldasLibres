from django.db import models


class Tarifa(models.Model):
    anno = models.PositiveIntegerField()
    tipo_vehiculo = models.CharField(max_length=10)
    por_hora = models.PositiveIntegerField()

    class Meta:
        verbose_name =  'tarifa'
        ordering = ['anno']

    def __str__(self):
        return str(self.anno)
