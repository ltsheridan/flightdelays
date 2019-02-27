from flightdelays.models import Flight, Airport, Airline, Aircraft, State, City, Country
from rest_framework import response, serializers, status


class AircraftSerializer(serializers.ModelSerializer):

	class Meta:
		model = Aircraft
		fields = ('aircraft_id', 'tail_number')


class AirlineSerializer(serializers.ModelSerializer):

	class Meta:
		model = Airline
		fields = ('airline_id', 'iata_code', 'airline_name')


class AirportSerializer(serializers.ModelSerializer):

	class Meta:
		model = Airport
		fields = ('airport_id', 'iata_code', 'airport_name', 'city_id', 'state_id', 'country_id', 'latitude', 'longitude')


class FlightSerializer(serializers.ModelSerializer):

	class Meta:
		model = Flight
		fields = ('flight_id', 'airline_id', 'aircraft_id', 'origin_airport', 'destination_airport', 'arrival_delay')


class StateSerializer(serializers.ModelSerializer):

	class Meta:
		model = State
		fields = ('state_id', 'state_name', 'country_id')


class CitySerializer(serializers.ModelSerializer):

	class Meta:
		model = City
		fields = ('city_id', 'city_name', 'state_id')


class CountrySerializer(serializers.ModelSerializer):

	class Meta:
		model = Country
		fields = ('country_id', 'country_name')
