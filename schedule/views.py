from django.shortcuts import render, redirect,  get_object_or_404
from .models import Route, Schedule, Stop
from django.http import HttpResponse

def schedule_list(request):
    schedules = Schedule.objects.all()
    stops = Stop.objects.all()

    route_filter = request.GET.get('route')
    if route_filter:
        schedules = schedules.filter(route__id=route_filter)

    routes = Route.objects.all()
    return render(request, 'schedule/schedule_list.html', {'schedules': schedules, 'routes': routes, 'stops': stops})


def add_route(request):
    if request.method == "POST":
        route_name = request.POST.get('route_name')
        if route_name:
            route = Route(name=route_name)
            route.save()
            return redirect('add_schedule')
    return render(request, 'schedule/add_route.html')

def add_schedule(request):
    if request.method == "POST":
        route_id = request.POST.get('route')
        departure_time = request.POST.get('departure_time')
        arrival_time = request.POST.get('arrival_time')
        stops_ids = request.POST.getlist('stops[]')  # Отримання списку зупинок

        if route_id and departure_time and arrival_time:
            route = Route.objects.get(id=route_id)

            schedule = Schedule(
                route=route,
                departure_time=departure_time,
                arrival_time=arrival_time
            )
            schedule.save()
            
            # Додавання зупинок до ManyToMany відносин
            for stop_id in stops_ids:
                stop = Stop.objects.get(id=stop_id)
                schedule.stops.add(stop)
            
            return redirect('schedule_list')
        else:
            return HttpResponse("Будь ласка, заповніть всі поля.", status=400)
    else:
        routes = Route.objects.all()
        stops = Stop.objects.all()
        return render(request, 'schedule/add_schedule.html', {'routes': routes, 'stops': stops})
    
def delete_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    if request.method == "POST":
        schedule.delete()
        return redirect('schedule_list')
    return render(request, 'schedule/delete_confirmation.html', {'schedule': schedule})

def edit_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)

    if request.method == "POST":
        route_id = request.POST.get('route')
        departure_time = request.POST.get('departure_time')
        arrival_time = request.POST.get('arrival_time')
        stops_ids = request.POST.getlist('stops')

        if route_id and departure_time and arrival_time:
            route = Route.objects.get(id=route_id)

            schedule.route = route
            schedule.departure_time = departure_time
            schedule.arrival_time = arrival_time
            schedule.stops.clear()
            
            for stop_id in stops_ids:
                stop = Stop.objects.get(id=stop_id)
                schedule.stops.add(stop)

            schedule.save()
            return redirect('schedule_list')
        else:
            return HttpResponse("Будь ласка, заповніть всі поля.", status=400)

    else:
        routes = Route.objects.all()
        stops = Stop.objects.all()
        return render(request, 'schedule/edit_schedule.html', {'schedule': schedule, 'routes': routes, 'stops': stops})
    
def add_stop(request):
    if request.method == "POST":
        location = request.POST.get('location')
        if location:
            stop = Stop(location=location)
            stop.save()
            return redirect('schedule_list')
    return render(request, 'schedule/add_stop.html')