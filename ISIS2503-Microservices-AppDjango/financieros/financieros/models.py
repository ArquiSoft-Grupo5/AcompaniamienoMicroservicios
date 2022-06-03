from django.db import models

class Cita(models.Model):
    estudiante = models.IntegerField(null=False, default=None)
    credits = models.FloatField(null=True, blank=True, default=None)
    valor = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.credits, self.valor)