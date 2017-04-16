from __future__ import unicode_literals

from django.db import models


class Atm(models.Model):
    ref = models.IntegerField(primary_key=True)
    serial = models.CharField(max_length=32)
    number = models.CharField(max_length=32)
    producer = models.CharField(max_length=32)
    model = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    address = models.CharField(max_length=1024)

    def __str__(self):
        return '{}: {}'.format(self.producer, self.serial)