from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Flight, Airport, Airline, Aircraft
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import Count
from .forms import FlightForm

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
	template_name = 'flightdelays/airports.html'
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
	template_name = 'flightdelays/flight.html'
	paginate_by = 50

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Flight.objects.annotate(Count('arrival_delay')).order_by('-arrival_delay__count')[:50]

@method_decorator(login_required, name='dispatch')
class FlightDetailView(generic.DetailView):
	model = Flight
	context_object_name = 'flight_detail'
	template_name = 'flightdelays/flight_detail.html'


@method_decorator(login_required, name='dispatch')
class FlightUpdateView(generic.UpdateView):
	model = Flight
	form_class = FlightForm
	context_object_name = 'flight'
	success_message = "Flight updated successfully"
	template_name = 'flightdelays/flight_update.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		site = form.save(commit=False)
		site.save()
		return HttpResponseRedirect(site.get_absolute_url())
