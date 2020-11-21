from django.db.models import Max
from django.test import Client, TestCase

from .models import Airport, Flight, Passenger

# Create your tests here.
class FlightTestCase(TestCase):
    def setUp(self):
        """Sets up tests"""

        # Create test airports
        a1 = Airport.objects.create(code='AAA', city='City A')
        a2 = Airport.objects.create(code='BBB', city='City B')

        # create test flights
        Flight.objects.create(origin=a1, destination=a2, duration=100)
        Flight.objects.create(origin=a1, destination=a1, duration=200)
        Flight.objects.create(origin=a1, destination=a2, duration=-100)

    def test_departures_count(self):
        a = Airport.objects.get(code='AAA')
        self.assertEqual(a.departures.count(), 3)

    def test_arrivals_count(self):
        a = Airport.objects.get(code='AAA')
        self.assertEqual(a.arrivals.count(), 1)

    def test_valid_flight(self):
        a1 = Airport.objects.get(code='AAA')
        a2 = Airport.objects.get(code='BBB')
        f = Flight.objects.get(origin=a1, destination=a2, duration=100)
        self.assertTrue(f.is_valid_flight())

    def test_invalid_flight_destination(self):
        a1 = Airport.objects.get(code='AAA')
        f = Flight.objects.get(origin=a1, destination=a1)
        self.assertFalse(f.is_valid_flight())

    def test_invalid_flight_duration(self):
        a1 = Airport.objects.get(code='AAA')
        a2 = Airport.objects.get(code='BBB')
        f = Flight.objects.get(origin=a1, destination=a2, duration=-100)
        self.assertFalse(f.is_valid_flight())

    def test_index(self):
        """Tests index.html webpage"""
        c = Client()
        response = c.get('/flights/')
        # 200 means the page is working
        self.assertEqual(response.status_code, 200)
        # context accesses the python dictionary passed to a django render page
        self.assertEqual(response.context['flights'].count(), 3)

    def test_valid_flight_page(self):
        """Tests the flights webpage"""
        a1 = Airport.objects.get(code='AAA')
        f = Flight.objects.get(origin=a1, destination=a1)

        c = Client()
        response = c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code, 200)

    # def test_invalid_flight_page(self):
    #     """Testing an invalid flight id"""
    #     max_id = Flight.objects.all().aggregate(Max('id'))['id__max']
    #
    #     c = Client()
    #     # should return an error because there is no flight with id greater than max_id
    #     response = c.get(f"/flights/{max_id + 1}")
    #     self.assertEqual(response.status_code, 404)

    def test_flight_page_passengers(self):
        """Test that the correct number of passengers shows up for a flight"""
        f = Flight.objects.get(pk=1)
        p = Passenger.objects.create(first='Alice', last='Adams')
        f.passengers.add(p)

        c = Client()
        response = c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['passengers'].count(), 1)
