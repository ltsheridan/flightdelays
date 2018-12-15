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
	model = Flight
	context_object_name = 'flights'
	template_name = 'flightdelays/flights.html'
	paginate_by = 50


class FlightDetailView(generic.DetailView):
	model = Flight
	context_object_name = 'flights'
	template_name = 'flights/flight_detail.html'
