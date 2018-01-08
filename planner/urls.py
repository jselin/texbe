from django.urls import path

from . import views

app_name = 'planner'

urlpatterns = [
    path('', views.PlanListView.as_view(), name='plan_list'),
    path('plans', views.PlanListView.as_view(), name='plan_list'),
    path('plans/<int:pk>', views.PlanDetailView.as_view(), name='plan_detail'),
    path('plans/create', views.PlanCreate.as_view(), name='plan_create'),
    path('yarns', views.YarnListView.as_view(), name='yarns'),
    path('yarns/<int:pk>', views.YarnDetailView.as_view(), name='yarn_detail'),
    path('yarns/create', views.YarnCreate.as_view(), name='yarn_create'),
    path('yarns/<int:pk>/edit', views.YarnUpdate.as_view(), name='yarn_edit'),
    path('yarns/<int:pk>/delete', views.YarnDelete.as_view(), name='yarn_delete'),
]