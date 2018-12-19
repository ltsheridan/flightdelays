from django.db import models
from django.urls import reverse

class Aircraft(models.Model):
    aircraft_id = models.AutoField(primary_key=True)
    tail_number = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'aircraft'

    def __str__(self):
        return self.tail_number


class Airline(models.Model):
    airline_id = models.AutoField(primary_key=True)
    iata_code = models.CharField(unique=True, max_length=3)
    airline_name = models.CharField(unique=True, max_length=100)

    # airport = models.ManyToManyField(Airport, through='Flight')

    class Meta:
        managed = False
        db_table = 'airline'
        verbose_name = 'Flight delay'
        verbose_name_plural = 'Flight delays'

    def __str__(self):
        return self.airline_name

class Airport(models.Model):
    airport_id = models.AutoField(primary_key=True)
    iata_code = models.CharField(unique=True, max_length=3)
    airport_name = models.CharField(max_length=255)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=3)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

    airline = models.ManyToManyField(Airline, through='Flight')

    class Meta:
        managed = False
        db_table = 'airport'
        verbose_name = 'Flight delay'
        verbose_name_plural = 'Flight delays'


    def __str__(self):
        return self.airport_name

class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    time_year = models.IntegerField()
    time_month = models.IntegerField()
    time_day = models.IntegerField()
    day_of_week = models.IntegerField()
    airline = models.ForeignKey('Airline', models.DO_NOTHING)
    #aircraft = models.ForeignKey(Aircraft, models.DO_NOTHING, blank=True, null=True)
    # airport = models.ForeignKey(Airport, on_delete=models.PROTECT, null=False, related_name='origin')
    airport = models.ForeignKey('Airport', models.DO_NOTHING)
    flight_number = models.IntegerField()
    scheduled_departure = models.IntegerField()
    departure_time = models.CharField(max_length=50)
    departure_delay = models.CharField(max_length=50)
    taxi_out = models.CharField(max_length=50)
    wheels_off = models.CharField(max_length=50)
    scheduled_time = models.CharField(max_length=50)
    elapsed_time = models.CharField(max_length=50)
    air_time = models.CharField(max_length=50)
    distance = models.IntegerField()
    wheels_on = models.CharField(max_length=50)
    taxi_in = models.CharField(max_length=50)
    scheduled_arrival = models.IntegerField()
    arrival_time = models.CharField(max_length=50)
    arrival_delay = models.CharField(max_length=50)
    diverted = models.IntegerField()
    cancelled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'flight'
        verbose_name = 'Flight delay'
        verbose_name_plural = 'Flight delays'
