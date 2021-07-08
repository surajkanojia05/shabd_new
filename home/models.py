
from django.db import models


# Create your models here.
class ghazal_home(models.Model):
    ghazal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    tags = models.CharField(max_length=500)
    writer = models.CharField(max_length=100)
    shayari = models.CharField(max_length=5000)

    def __str__(Self):
        return Self.name

class new_ghazal(models.Model):
    ghazal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    tags = models.CharField(max_length=500)
    writer = models.CharField(max_length=100)
    shayari = models.CharField(max_length=5000)

    def __str__(Self):
        return Self.name

class famous_ghazal(models.Model):
    ghazal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    tags = models.CharField(max_length=500)
    writer = models.CharField(max_length=100)
    shayari = models.CharField(max_length=5000)

    def __str__(Self):
        return Self.name   