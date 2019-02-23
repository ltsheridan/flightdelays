from django.db import models
from django.urls import reverse
import django_filters

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
    city = models.ForeignKey('City', on_delete=models.PROTECT, max_length=45)
    state = models.ForeignKey('State', on_delete=models.PROTECT, max_length=2)
    country = models.ForeignKey('Country', on_delete=models.PROTECT, max_length=3)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)


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
    airline = models.ForeignKey(Airline, models.DO_NOTHING)
    aircraft = models.ForeignKey(Aircraft, models.DO_NOTHING)
    origin_airport = models.ForeignKey(Airport, on_delete=models.PROTECT, null=False, related_name='origin_airport')
    destination_airport = models.ForeignKey(Airport, on_delete=models.PROTECT, null=False, related_name='destination_airport')
    flight_number = models.IntegerField()
    scheduled_departure = models.IntegerField()
    departure_time = models.IntegerField()
    departure_delay = models.IntegerField()
    taxi_out = models.IntegerField()
    wheels_off = models.IntegerField()
    scheduled_time = models.IntegerField()
    elapsed_time = models.IntegerField()
    air_time = models.IntegerField()
    distance = models.IntegerField()
    wheels_on = models.IntegerField()
    taxi_in = models.IntegerField()
    scheduled_arrival = models.IntegerField()
    arrival_time = models.IntegerField()
    arrival_delay = models.IntegerField()
    diverted = models.IntegerField()
    cancelled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'flight'
        verbose_name = 'Flight delay'
        verbose_name_plural = 'Flight delays'

    def __str__(self):
        return self.origin_airport

    def get_absolute_url(self):
        return reverse('flight_detail', kwargs={'pk': self.pk})

class State(models.Model):
    state_id=models.AutoField(primary_key=True)
    state_name=models.CharField(unique=True, max_length=50)
    country=models.ForeignKey('Country', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'state'
        verbose_name = 'Flight delay'
        verbose_name_plural = 'Flight delays'

class City(models.Model):
    city_id=models.AutoField(primary_key=True)
    city_name=models.CharField(max_length=50)
    state=models.ForeignKey('State', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'city'
        verbose_name = 'Flight delay'
        verbose_name_plural = 'Flight delays'

class Country(models.Model):
    country_id=models.AutoField(primary_key=True)
    country_name=models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'country'
        verbose_name = 'Flight delay'
        verbose_name_plural = 'Flight delays'
