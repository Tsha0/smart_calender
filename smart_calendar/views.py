from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"smart_calendar/calendar.html")

def add_event(request):

    
    return render(request,"template.add_event.html")
# Create your views here.
