from django.db import models

class FallenSoldier(models.Model):
    name = models.CharField(max_length=100)
    reason_of_death = models.TextField()
    place_killed = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name

class ArrestedPerson(models.Model):
    name = models.CharField(max_length=100)
    police_station = models.CharField(max_length=100)
    has_representation = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return self.name

class MissingPerson(models.Model):
    name = models.CharField(max_length=100)
    time_of_missing = models.DateTimeField()
    found = models.BooleanField(default=False)
    date_found = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name