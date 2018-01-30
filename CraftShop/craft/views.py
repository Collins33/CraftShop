from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import categories,Craft,NewsLetterSubscription
from .forms import NewsLetterForm,NewCraftForm
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .email import sendEmail
from django.contrib.auth.decorators import login_required
from cart.forms import CartAddProductForm
from cart.cart import Cart

# Create your views here.
def welcome(request):
    date=dt.date.today()
    crafts=Craft.todayCraft()
    if request.method == 'POST':
        #CHECK IF REQUEST IS A POST REQUEST
        form=NewsLetterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['your_name']
            email=form.cleaned_data['email']
            recipient=NewsLetterSubscription(name=name,email=email)
            recipient.save()
            sendEmail(name,email)
            HttpResponseRedirect('welcome')

    else:
        form=NewsLetterForm()


    return render(request, 'index.html',{'date':date, 'crafts':crafts,"form":form})



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
    cart_form=CartAddProductForm()
    try:
        craft=Craft.objects.get(id=craft_id)
    except DoesNotExist:
        raise Http404()

    return render(request,"craft.html",{"craft":craft,"form":cart_form})



@login_required(login_url='/accounts/login/')
def all_craft(request):
    craft=Craft.allCrafts()
    return render(request, 'showcase.html',{"crafts":craft})


@login_required(login_url="/accounts/login/")
def new_craft(request):
    current_user=request.user
    if request.method == "POST":
        form=NewCraftForm(request.POST,request.FILES)
        if form.is_valid():
            craft=form.save(commit=False)
            craft.artist=current_user
            craft.save()
    else:
        form=NewCraftForm()
    return render(request,"newCraft.html",{"form":form})
