from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        # a variable containing all of the flights
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id) # pk represents the primary key (the id in this case)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(), #uses the realated name for passengers
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        # adds the flight to the passengers flight list
        passenger.flights.add(flight)
        # redirects the user to the flight page
        return HttpResponseRedirect(reverse("flight", args=[flight.id]))
