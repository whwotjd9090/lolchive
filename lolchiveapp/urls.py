from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('replays/', views.replays, name='replays')
]