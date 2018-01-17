from django.urls import path
from django.views.generic.base import RedirectView
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'planner'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('plans', login_required(views.PlanListView.as_view()), name='plans'),
    path('plans/create', views.PlanCreate.as_view(), name='plan_create'),
    path('plans/<int:pk>', views.PlanDetailView.as_view(), name='plan_detail'),
    path('plans/<int:pk>/update', views.PlanUpdate.as_view(), name='plan_update'),
    path('plans/<int:pk>/delete', views.PlanDelete.as_view(), name='plan_delete'),
    path('yarns', views.YarnListView.as_view(), name='yarns'),
    path('yarns/create', views.YarnCreate.as_view(), name='yarn_create'),
    path('yarns/<int:pk>', views.YarnDetailView.as_view(), name='yarn_detail'),
    path('yarns/<int:pk>/update', views.YarnUpdate.as_view(), name='yarn_update'),
    path('yarns/<int:pk>/delete', views.YarnDelete.as_view(), name='yarn_delete'),
    path('yarnmanfacturers/create', views.YarnManufacturerCreate.as_view(), name='yarn_manufacturer_create'),
 ]   