import django_filters
from flightdelays.models import Flight, Aircraft, Airline, Airport, State, City, Country


class FlightFilter(django_filters.FilterSet):
	arrival_delay = django_filters.CharFilter(
		field_name='arrival_delay',
		label='Arrival delay time',
		lookup_expr='icontains'
	)

	origin_airport = django_filters.CharFilter(
		field_name='origin_airport',
		label='Origin airport',
		lookup_expr='icontains'
	)

	destination_airport = django_filters.CharFilter(
		field_name='destination_airport',
		label='Destination airport',
		lookup_expr='icontains'
	)
	airline = django_filters.ModelChoiceFilter(
		field_name='airline',
		label='Airline',
		queryset=Airline.objects.all().order_by('airline_name'),
		lookup_expr='exact'
	)


	class Meta:
		model = Flight
		# form = SearchForm
		fields = []
