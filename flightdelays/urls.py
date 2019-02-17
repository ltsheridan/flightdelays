from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
   path('', views.HomePageView.as_view(), name='home'),
   path('about/', views.AboutPageView.as_view(), name='about'),
   path('airports/', views.AirportListView.as_view(), name='airports'),
   path('airports/<int:pk>/', views.AirportDetailView.as_view(), name='airport_detail'),
   path('flights/', views.FlightListView.as_view(), name='flight'),
   path('flights/<int:pk>/', views.FlightDetailView.as_view(), name='flight_detail'),
   path('flights/<int:pk>/update/', views.FlightUpdateView.as_view(), name='flight_update')
]
