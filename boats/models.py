from django.db import models

# Create your models here.

class Officer(models.Model):
    name = models.CharField(max_length=256)
    rank = models.ForeignKey('Rank', on_delete=models.CASCADE)
    ship_assignment = models.ForeignKey('Ship', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Rank(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Ship(models.Model):
    name = models.CharField(max_length=256)
    registry = models.CharField(max_length=256)
    captain = models.OneToOneField('Officer', default=None, on_delete=models.CASCADE, blank=True, null=True)
    ship_class = models.CharField(max_length=256)
    status = models.CharField(max_length=256)

    def __str__(self):
        return self.name
