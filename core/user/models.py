from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import MEDIA_URL, STATIC_URL


class User(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    CATEGORIA_CHOICES = [
        ('SUPERVISOR', 'SUPERVISOR'),
        ('MAQUINISTA', 'MAQUINISTA'),
        ('1ER AYUDANTE', '1ER AYUDANTE'),
        ('2DO AYUDANTE', '2DO AYUDANTE'),
        ('MECANICO', 'MECÁNICO'),
    ]

    categoria = models.TextField(choices=CATEGORIA_CHOICES)

    def toJSON(self):
        item= model_to_dict(self)
        item['categoria']= self.categoria.toJSON()