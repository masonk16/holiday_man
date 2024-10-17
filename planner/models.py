from django.db import models
from django.contrib.postgres.fields import DateRangeField
from core.models import MyUser


class Destination(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Trip(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    destinations = models.ManyToManyField(Destination)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('start_date', 'end_date', 'owner')

    def __str__(self):
        return f'{self.owner.last_name}, {self.owner.first_name}: {self.start_date} - {self.end_date}'