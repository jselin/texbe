from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import json

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Yarn
from .models import YarnManufacturer
from .models import Plan    


def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    user = request.user
    auth0user = user.social_auth.get(provider="auth0")
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture']
    }
    
    return render(request, 'planner/dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })

class YarnListView(generic.ListView):
    model = Yarn
    context_object_name = 'yarns'

    def get_queryset(self):
        return Yarn.objects.order_by('manufacturer')

class YarnDetailView(generic.DetailView):
    model = Yarn

class PlanListView(generic.ListView):
    model = Plan
    context_object_name = 'plans'

    def get_queryset(self):
        return Plan.objects.order_by('name')

class YarnCreate(CreateView):
    model = Yarn
    fields = ['manufacturer', 'name', 'material', 'number', 'numbering_system', 'sett']
    success_url = '/planner/yarns'

class YarnUpdate(UpdateView):
    model = Yarn
    fields = ['manufacturer', 'name', 'material', 'number', 'numbering_system', 'sett']

class YarnDelete(DeleteView):
    model = Yarn
    success_url = reverse_lazy('planner:yarns')

class PlanDetailView(generic.DetailView):
    model = Plan

class PlanCreate(CreateView):
    model = Plan
    fields = ['name', 'finished_lenght', 'warp_shrinkage', 'warp_take_up', 'finished_width', 'weft_shrinkage', 'weft_draw_in', 'picks_per_cm', 'ends_per_cm', 'test_lenght', 'tying_lenght', 'loom_waste_lenght', 'fringe_lenght', 'selvedge_width', 'warp_yarn', 'weft_yarn']
    success_url = reverse_lazy('planner:plans')

class PlanUpdate(UpdateView):
    model = Plan
    fields = ['name', 'finished_lenght', 'warp_shrinkage', 'warp_take_up', 'finished_width', 'weft_shrinkage', 'weft_draw_in', 'picks_per_cm', 'ends_per_cm', 'test_lenght', 'tying_lenght', 'loom_waste_lenght', 'fringe_lenght', 'selvedge_width', 'warp_yarn', 'weft_yarn']
    success_url = reverse_lazy('planner:plans')


class PlanDelete(DeleteView):
    model = Plan
    success_url = reverse_lazy('planner:plans')

class YarnManufacturerCreate(CreateView):
    model = YarnManufacturer
    fields = ['name']
    success_url = reverse_lazy('planner:yarn_create')