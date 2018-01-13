from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Artist,categories,Craft

# Create your views here.
def welcome(request):
    date=dt.date.today()
    crafts=Craft.todayCraft()
    return render(request, 'index.html',{'date':date, 'crafts':crafts})



def search_result(request):
    if "craft" in request.GET and request.GET["craft"]:
        search_term=request.GET.get("craft")
        search_craft=Craft.search_by_name(search_term)
        message=f"{search_term}"

        return render(request, 'search.html', {"message":message, "crafts":search_craft})

    else:
        message="YOU HAVE NOT SEARCHED FOR ANYTHING"
        return render(request, 'search.html', {"message":message})



def craft(request,craft_id):
    try:
        craft=Craft.objects.get(id=craft_id)
    except DoesNotExist:
        raise Http404()

    return render(request,"craft.html",{"craft":craft})        
