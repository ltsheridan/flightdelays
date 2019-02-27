from django.shortcuts import render
from flightdelays.models import Flight, Airport, Aircraft
from api.serializers import FlightSerializer
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response


class FlightViewSet(viewsets.ModelViewSet):

	queryset = Flight.objects.select_related('arrival_delay').order_by('-arrival_delay')[:50]
	serializer_class = FlightSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def delete(self, request, pk, format=None):
		site = self.get_object(pk)
		self.perform_destroy(self, site)

		return Response(status=status.HTTP_204_NO_CONTENT)

	def perform_destroy(self, instance):
		instance.delete()
