from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
   path('', views.HomePageView.as_view(), name='home'),
   path('about/', views.AboutPageView.as_view(), name='about'),
   path('flights/', views.FlightListView.as_view(), name='flights'),
   path('flights/<int:pk>/',views.AirportDetailView.as_view(), name='flight_detail')
]
