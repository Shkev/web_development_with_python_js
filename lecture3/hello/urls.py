# file contains the urls that can be accessed from the app
from django.urls import path

from . import views

# each link accesses a view in the views file
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"), #allows dynamically applying views in urls
    path("shayan", views.shayan, name="shayan"),
    path("david", views.david, name="david"),
]
