from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Yarn


class YarnListView(generic.ListView):
    model = Yarn
    context_object_name = 'yarns'

    def get_queryset(self):
        return Yarn.objects.order_by('manufacturer')

class YarnDetailView(generic.DetailView):
    model = Yarn

def IndexView(request):
    return render(request, 'planner/index.html')



