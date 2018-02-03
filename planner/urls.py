from django.urls import path
from django.views.generic.base import RedirectView
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'planner'

urlpatterns = [
    #path('', views.Landing.as_view(), name='landing'),
    path('', views.index, name='index'),
    path('dashboard', login_required(views.dashboard), name='dashboard'),
    path('plans', login_required(views.PlanListView.as_view()), name='plans'),
    path('plans/create', login_required(views.plan_create), name='plan_create'),
    path('plans/<int:pk>', login_required(views.PlanDetailView.as_view()), name='plan_detail'),
    path('plans/<int:pk>/delete', login_required(views.PlanDelete.as_view()), name='plan_delete'),
    path('plans/<int:pk>/update', login_required(views.plan), name='plan_update'),
    path('yarns', login_required(views.YarnListView.as_view()), name='yarns'),
    path('yarns/create', login_required(views.YarnCreate.as_view()), name='yarn_create'),
    path('yarns/<int:pk>', login_required(views.YarnDetailView.as_view()), name='yarn_detail'),
    path('yarns/<int:pk>/update', login_required(views.YarnUpdate.as_view()), name='yarn_update'),
    path('yarns/<int:pk>/delete', login_required(views.YarnDelete.as_view()), name='yarn_delete'),
    path('yarnmanufacturers/create', login_required(views.YarnManufacturerCreate.as_view()), name='yarn_manufacturer_create'),
 ]   