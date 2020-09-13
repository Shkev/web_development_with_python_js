from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


# A class to store form values
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    # checks if the task variable exists in the current Sessions
    # if it isn't it creates a new variable
    if "tasks" not in request.session:
        # creating a new task list per user in a session
        request.session['tasks'] = list()
    return render(request, "tasks/index.html", {
        # the key of the given dict is the variable used in the html template file
        "tasks": request.session['tasks']
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['tasks'] += [task]
            #redicrects the user to a url
            #reverse() tells django to figure out the url based on the url name
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        # displays an empty form
        "form": NewTaskForm()
    })
