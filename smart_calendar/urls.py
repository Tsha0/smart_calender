from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('addevent/', views.add_event, name='add_event'),
    
]