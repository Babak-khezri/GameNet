from django.shortcuts import render, get_object_or_404
from .models import PlayTime
from system.models import System
from django.http import JsonResponse
from django.utils import timezone
import datetime
from payment.models import Payment
# Create your views here.


def reserve_system_view(request):
    search_system = None
    if request.method == 'POST':
        value = request.POST.get('systems')
        system = System.objects.get(pk=value)
        system.is_busy = True
        system.save()
        object = PlayTime(system=system)
        object.save()
        print("post")
    elif request.method == "GET":
        system_name = request.GET.get('search')
        try:
            search_system = System.objects.get(name=system_name)
            if not system.is_busy:
                search_system = None
        except:
            pass

    free_systems = System.objects.filter(is_busy=False)
    busy_systems = System.objects.filter(is_busy=True)
    context = {'busy_systems': busy_systems,
               'free_systems': free_systems, 'system': search_system}
    return render(request, 'reserve/reserve_system.html', context)


def close_time_view(request, pk):
    system = System.objects.get(pk=pk)
    system.is_busy = False
    system.save()
    playtime = system.play_times.last()
    employee = request.user
    payment = Payment(recorder=employee,
                      playtime=playtime,
                      amount=100,
                      system=system,
                      )
    payment.save()
    return reserve_system_view(request)


def calc_total_cost(request, pk):
    now = datetime.datetime.now(timezone.utc)
    playtime = get_object_or_404(PlayTime, pk=pk)
    total_time = (now - playtime.start_time).seconds
    hours = total_time//3600
    minutes = (total_time//60) % 60
    if hours == 0:
        total_cost = playtime.system.cost_per_hour // 2
    else:
        if minutes < 30:
            total_cost = playtime.system.cost_per_hour * hours
        else:
            total_cost = playtime.system.cost_per_hour * \
                hours + playtime.system.cost_per_hour // 2

    if hours < 10:
        hours = "0" + str(hours)
    if minutes < 10:
        minutes = "0" + str(minutes)
    total_time = str(hours) + ":" + str(minutes)

    data = {
        "total_cost": total_cost,
        "total_time": total_time,
    }
    return JsonResponse(data, status=200)
