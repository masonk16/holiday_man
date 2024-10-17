import os
import requests
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Trip, Destination
from .serializers import TripSerializer, DestinationSerializer
from dotenv import load_dotenv

load_dotenv()

BASE_WEATHER_URL = "http://api.weatherapi.com/v1/future.json"
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

class DestinationViewSet(viewsets.ViewSet):

    def list(self, request):
        destinations = []
        for destination in Destination.objects.all():
            result = requests.get(
                f'{BASE_WEATHER_URL}?key={WEATHER_API_KEY}&q={destination.name}&dt={request.query_params.get("travel_date")}')
            weather = result.json()
            dest_data = {
                "id": destination.id,
                "name": destination.name,
                "country": destination.country,
                "forecast": weather["forecast"]["forecastday"][0]["day"],
            }
            destinations.append(dest_data)
        return Response(destinations, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Destination.objects.all()
        destination = get_object_or_404(queryset, pk=pk)
        serializer = DestinationSerializer(destination)
        return Response(serializer.data)


class TripViewSet(viewsets.ViewSet):

    def list(self, request):
        trips = Trip.objects.filter(owner=request.user.id)
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Trip.objects.filter(owner=request.user.id)
        trip = get_object_or_404(queryset, pk=pk)
        serializer = TripSerializer(trip)
        return Response(serializer.data)

    def create(self, request):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        trip = get_object_or_404(Trip, pk=pk)
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)