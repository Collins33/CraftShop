from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    date=dt.date.today()
    return render(request,'index.html',{'date':date})
