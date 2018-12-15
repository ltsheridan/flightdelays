from django.contrib import admin

from django.contrib import admin

import flightdelays.models as models

# 
# @admin.register(models.Flight)
# class FlightAdmin(admin.ModelAdmin):
# 	fields = ['flight_number']
# 	list_display = ['flight_number']
# 	list_filter = ['flight_number']


@admin.register(models.Airline)
class AirlineAdmin(admin.ModelAdmin):
	fields = ['iata_code', 'airline_name']
	list_display = ['airline_name']
	ordering = ['airline_name']


@admin.register(models.Aircraft)
class AircraftAdmin(admin.ModelAdmin):
	fields = ['tail_number']
	list_display = ['tail_number']
	ordering = ['tail_number']


@admin.register(models.Airport)
class AirportAdmin(admin.ModelAdmin):
	fields = ['iata_code','airport_name', 'city', 'state', 'country', 'latitude', 'longitude']
	list_display = ['airport_name', 'city', 'state']
	ordering = ['airport_name', 'city', 'state']
