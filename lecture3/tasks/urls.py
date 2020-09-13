from django.urls import path

from . import views

# the app_name variable allows us to deal with namespace collisions
# we can reference which app we would like to access
app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]
