from rest_framework import serializers
from .models import Trip, Destination


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ["id", "name", "country"]


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ["id", "start_date", "end_date", "destinations", "owner"]
