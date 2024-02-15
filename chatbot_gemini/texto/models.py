from django.db import models


class Texto(models.Model):
    texto = models.CharField(max_length=1000)

    def __str__(self):
        return self.texto
