from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# A view is what the user will see on the site

# create a function for each view.
def index(request):
    # render allows you to load an entire html file instead of just a string
    return render(request, "hello/index.html")

def shayan(request):
    return HttpResponse("Hello, Shayan!")

def david(request):
    return HttpResponse("Hello, David!")

# generalized greeting function
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
