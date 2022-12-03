from multiprocessing import context
from django.shortcuts import render
from system.models import System
# Create your views here.


def home_view(request):
    free_systems = System.objects.filter(is_busy=False)
    busy_systems = System.objects.filter(is_busy=True)

    context = {
        'busy_systems_count': busy_systems.count(),
        'free_systems_count': free_systems.count(),
    }
    return render(request, 'gamenet/home_menu.html',context)


def contact_view(request):
    return render(request,'gamenet/contact.html')

def about_view(request):
    return render(request,'gamenet/about.html')