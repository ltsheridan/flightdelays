from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Flight, Airport, Airline, Aircraft


def index(request):
   return HttpResponse("Hello, world. You're at the 2015 Flight Delays index.")

class AboutPageView(generic.TemplateView):
	template_name = 'flightdelays/about.html'

class HomePageView(generic.TemplateView):
	template_name = 'flightdelays/home.html'


class FlightListView(generic.ListView):
	model = Airport
	context_object_name = 'airports'
	template_name = 'flightdelays/flights.html'
	paginate_by = 50

	def get_queryset(self):
		return Airport.objects.all()

class AirportDetailView(generic.DetailView):
	model = Airport
	context_object_name = 'airport_detail'
	template_name = 'flightdelays/airport_detail.html'

class FlightDetailView(generic.ListView):
	model = Flight
	context_object_name = 'flight_detail'
	template_name = 'flightdelays/flight_detail.html'
