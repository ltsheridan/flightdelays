from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Flight, Airport, Airline, Aircraft
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def index(request):
   return HttpResponse("Hello, world. You're at the 2015 Flight Delays index.")

class AboutPageView(generic.TemplateView):
	template_name = 'flightdelays/about.html'

class HomePageView(generic.TemplateView):
	template_name = 'flightdelays/home.html'

@method_decorator(login_required, name='dispatch')
class AirportListView(generic.ListView):
	model = Airport
	context_object_name = 'airports'
	template_name = 'flightdelays/flights.html'
	paginate_by = 50

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Airport.objects.all().order_by('airport_name')

@method_decorator(login_required, name='dispatch')
class AirportDetailView(generic.DetailView):
	model = Airport
	context_object_name = 'airport_detail'
	template_name = 'flightdelays/airport_detail.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

@method_decorator(login_required, name='dispatch')
class FlightListView(generic.ListView):
	model = Flight
	context_object_name = 'flights'
	template_name = 'flightdelays/flights.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

class FlightDetailView(generic.DetailView):
	model = Flight
	context_object_name = 'flight_detail'
	template_name = 'flightdelays/flight_detail.html'

	def get_queryset(self):
		return Flight.objects.all()
