from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Artist,categories,Craft

# Create your views here.
def welcome(request):
    date=dt.date.today()
    crafts=Craft.allCrafts()
    return render(request, 'index.html',{'date':date, 'crafts':crafts})
