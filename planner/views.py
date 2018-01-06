from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Yarn
from .models import YarnManufacturer


class YarnListView(generic.ListView):
    model = Yarn
    context_object_name = 'yarns'

    def get_queryset(self):
        return Yarn.objects.order_by('manufacturer')

class YarnDetailView(generic.DetailView):
    model = Yarn

def IndexView(request):
    return render(request, 'planner/index.html')

class YarnCreate(CreateView):
    model = Yarn
    fields = ['manufacturer', 'name', 'material', 'number', 'numbering_system', 'sett', 'sett_unit']
    success_url = '/planner/yarns'

class YarnUpdate(UpdateView):
    model = Yarn
    fields = ['manufacturer', 'name', 'material', 'number', 'numbering_system', 'sett', 'sett_unit']

class YarnDelete(DeleteView):
    model = Yarn
    success_url = reverse_lazy('planner:yarns')
