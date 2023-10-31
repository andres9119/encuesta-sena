from django.db import models


class RespuestaEncuesta(models.Model):

    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

    pregunta1 = models.TextField()
    pregunta2 = models.TextField()
    pregunta3 = models.TextField()
    pregunta4 = models.CharField(max_length=20, choices=[
        ('efectivo', 'Efectivo'),
        ('transferencia', 'Transferencia'),
        ('datafono', 'Datafono'),
        ('todas', 'Todas'),
    ])
    pregunta5 = models.TextField()
    pregunta6 = models.TextField()
    pregunta7 = models.CharField(max_length=20, choices=[
        ('de 1 a 5 años', 'De 1 a 5 años'),
        ('de 6 a 10 años', 'De 6 a 10 años'),
        ('de 11 a 15 años', 'De 11 a 15 años'),
        ('más de 15 años', 'Más de 15 años'),

    ])
    pregunta8 = models.TextField()
    pregunta9 = models.TextField()
    pregunta10 = models.TextField()
    pregunta11 = models.CharField(max_length=20, choices=[
        ('una persona', 'Una persona'),
        ('dos personas', 'Dos personas'),
        ('tres personas', 'Tres personas'),
        ('mas de tres personas', 'Mas de tres personas'),
    ])
    pregunta12 = models.TextField()

    def __str__(self):
        return f'Respuesta de {self.nombre}'
