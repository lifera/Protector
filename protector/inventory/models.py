from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AircraftType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    part_number = models.CharField(max_length=200, unique=True)
    alternative_part_number = ArrayField(base_field=models.CharField(max_length=200, blank=True),
                                         blank=True, null=True)
    descriptions = models.TextField(blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)
    aircraft_type = models.ManyToManyField(AircraftType, blank=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.part_number

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = datetime.now()
        self.save()

    def get_absolute_url(self):
        return reverse('inventory')
