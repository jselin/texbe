from django.urls import path

from . import views

app_name = 'planner'

urlpatterns = [
    path('', views.IndexView),
    path('yarn', views.YarnListView.as_view(), name='yarn'),
    path('yarn/<int:pk>', views.YarnDetailView.as_view(), name='yarn_detail'),
]