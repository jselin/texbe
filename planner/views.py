from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import json
from django.template import Context

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Yarn
from .models import YarnManufacturer
from .models import Plan    

from django import forms
from .forms import PlanForm

def index(request):
    return render(request, 'index.html')

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

class PlanDelete(DeleteView):
    model = Plan
    success_url = reverse_lazy('planner:plans')

class YarnManufacturerCreate(CreateView):
    model = YarnManufacturer
    fields = ['name']
    success_url = reverse_lazy('planner:yarn_create')

def plan(request, pk):
    instance = Plan.objects.get(pk=pk)

    if request.method == 'POST':
        form = PlanForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            plan_calculate(instance)

            if request.POST.get('save'):
                instance.save()
                return HttpResponseRedirect(reverse_lazy('planner:plans'))
            else:  # calculate only
                form = PlanForm(instance=instance)
                return render(request, 'planner/plan.html', {'form': form})
    else: 
        form = PlanForm(instance=instance)

    return render(request, 'planner/plan.html', {'form': form})

def plan_calculate(instance):
    instance.warp_lenght = instance.finished_lenght + instance.test_lenght
    
