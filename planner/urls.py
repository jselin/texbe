from django.urls import path

from . import views

app_name = 'planner'

urlpatterns = [
    path('', views.IndexView),
    path('yarns', views.YarnListView.as_view(), name='yarns'),
    path('yarns/<int:pk>', views.YarnDetailView.as_view(), name='yarn_detail'),
    path('yarns/add', views.YarnCreate.as_view(), name='yarn_add'),
    path('yarns/<int:pk>/edit', views.YarnUpdate.as_view(), name='yarn_edit'),
    path('yarns/<int:pk>/delete', views.YarnDelete.as_view(), name='yarn_delete'),
]