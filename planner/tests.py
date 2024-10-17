from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .views import TripViewSet, DestinationViewSet
from .models import Destination, Trip
from core.models import MyUser


class TripViewSetTestCase(APITestCase):

    def setUp(self):
        MyUser.objects.create(username='test', email='test@mail.com', password='pass123')
        Destination.objects.create(name="Kigali", country="Rwanda")
        Destination.objects.create(name="Seoul", country="Korea")
        Destination.objects.create(name="Southampton", country="United Kingdom")

    # def test_create_trip(self):
    #     url = reverse('planner:trips-create')
    #     data = {
    #         "start_date": "2020-01-01",
    #         "end_date": "2020-01-02",
    #         "destinations": ["1", "3"],
    #         "owner": 1,
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Trip.objects.count(), 1)

    def test_list_trips(self):
        url = reverse('planner:trips-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DestinationViewSetTestCase(APITestCase):

    def setUp(self):
        Destination.objects.create(name="Kigali", country="Rwanda")
        Destination.objects.create(name="Seoul", country="Korea")
        Destination.objects.create(name="Southampton", country="United Kingdom")

    def test_list_destinations(self):
        url = reverse('planner:destinations-list')
        response = self.client.get(url, query_params={"travel_date": "2025-01-01"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)\

    def test_retrieve_destination(self):
        url = reverse('planner:destination-detail', kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)