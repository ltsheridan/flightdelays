from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
   path('', views.HomePageView.as_view(), name='home'),
   path('about/', views.AboutPageView.as_view(), name='about'),
   path('flights/', views.AirportListView.as_view(), name='airports'),
   path('flights/<int:pk>/',views.AirportDetailView.as_view(), name='flight_detail'),
   # path('flights/<int:pk/',views.FlightDetailView.as_view(), name='flight_details_new')
]
