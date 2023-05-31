from django.shortcuts import render, redirect
from .models import Event
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Q


# Create your views here.


@login_required
def home(request):
    # We have fetched all the details of the events
    std = Event.objects.all()
    # so all of the data in std will be retrieved to home page
    return render(request, 'std/home.html', {'std': std})


@login_required
def evt_add(request):
    return render(request, "std/add_evt.html", {})


@login_required
def evt_add(request):
    if request.method == 'POST':
        print("Applied")
        # it takes the inputs we have typed
        std_name = request.POST.get("std_name")
        std_email = request.POST.get("std_email")
        std_phone = request.POST.get("std_phone")
        std_type = request.POST.get("std_type")
        std_date = request.POST.get("std_date")
        std_location = request.POST.get("std_location")
        std_description = request.POST.get("std_description")

        # object creation for model class
        e = Event()
        e.name = std_name
        e.email = std_email
        e.phone = std_phone
        e.type = std_type
        e.date = std_date
        e.location = std_location
        e.description = std_description

        e.save()

        # after inputing info the information displays on home page
        return redirect('/std/home')

    # renders an empty form for adding new events
    return render(request, "std/add_evt.html", {})


@login_required
def delete_evt(request, name):
    # when hovering on delete btn, number shows in order for each row below
    e = Event.objects.get(pk=name)
    e.delete()
    # after clicking on delete it should return to home page
    return redirect("/std/home")


@login_required
def update_evt(request, name):
    std = Event.objects.get(pk=name)
    return render(request, "std/update_evt.html", {'std': std})


# after updating the update task should save
@login_required
def do_update_evt(request, name):
    evt_name = request.POST.get("std_name")
    evt_email = request.POST.get("std_email")
    evt_phone = request.POST.get("std_phone")
    evt_type = request.POST.get("std_type")
    evt_date = request.POST.get("std_date")
    evt_location = request.POST.get("std_location")
    evt_description = request.POST.get("std_description")

    evt = Event.objects.get(pk=name)

    evt.name = evt_name
    evt.email = evt_email
    evt.phone = evt_phone
    evt.type = evt_type
    evt.date = evt_date
    evt.location = evt_location
    evt.description = evt_description

    evt.save()

    # after clicking on update the changes should me made at the home page
    return redirect("/std/home")

# view request button to view all the details of the event


@login_required
def detail(request, name):
    std = get_object_or_404(Event, pk=name)
    return render(request, 'std/detail.html', {'std': std})


@login_required
def search_events(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        events = Event.objects.filter(
            Q(name__contains=searched) | Q(type__contains=searched))
        return render(request, 'std/search_results.html', {'searched': searched, 'events': events})
    else:
        return render(request, 'std/search_results.html', {})
