import django_filters
from flightdelays.models import Flight, Aircraft, Airline, Airport, State, City, Country


class FlightFilter(django_filters.FilterSet):
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
