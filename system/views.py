from .forms import SystemForm
from django.shortcuts import render
from .models import System
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
# Create your views here.


def system_list_view(request):
    systems = System.objects.all()
    form = SystemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            ram = form.cleaned_data['ram']
            graphic = form.cleaned_data['graphic']
            cph = form.cleaned_data['cost_per_hour']
            system = System(name=name,ram=ram,graphic=graphic,cost_per_hour=cph)
            system.save()
            
    context = {
        'systems':systems,
        'form': form,
    }
    return render(request, 'system/system_list.html',context)


class SystemUpdateView(UpdateView):
    model = System
    fields = ['name','ram','graphic','cost_per_hour']
    template_name = 'system/system_update.html'
    success_url = reverse_lazy('system:system_list')

def system_delete_view(request,pk):
    try:
        system = System.objects.get(pk=pk)
        system.delete()
    except Exception:
        pass
    return reverse_lazy('system:system_list')