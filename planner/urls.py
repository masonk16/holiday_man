from django.urls import path
from .views import TripViewSet, DestinationViewSet

app_name = 'planner'

urlpatterns = [
    path("trips/", TripViewSet.as_view({'get': 'list'}),
         name="trips-list"),
    path("trips/<int:pk>", TripViewSet.as_view({'get': 'retrieve'}),
         name="trip-detail"),
    path("trips/create/", TripViewSet.as_view({'post': 'create'}),
         name="trips-create"),
    path("trips/<int:pk>/delete/", TripViewSet.as_view({'delete': 'destroy'})),
    path("destinations/", DestinationViewSet.as_view({'get': 'list'}),
         name="destinations-list"),
    path("destinations/<int:pk>", DestinationViewSet.as_view({'get': 'retrieve'}),
         name="destination-detail"),
]