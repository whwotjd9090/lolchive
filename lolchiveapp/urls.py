from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('replayupdate/', views.replay_update, name='replay update')
]