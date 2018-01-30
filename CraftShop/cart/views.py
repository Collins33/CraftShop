from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
import datetime as dt
from craft.models import categories,Craft,NewsLetterSubscription
from django.http import HttpResponse,Http404,HttpResponseRedirect
from craft.email import sendEmail
from django.contrib.auth.decorators import login_required
from .cart import Cart
from .forms import CartAddProductForm
# Create your views here.

# @require_POST#this form only allows post requests
def cart_add(request,craft_id):
    cart=Cart(request)#cart instance
    craft=get_object_or_404(Craft,id=craft_id)#get craft that matches the id
    form=CartAddProductForm(request.POST)#validate the form
    if form.is_valid():
        cd=form.cleaned_data
        cart.add(craft=craft,quantity=cd['quantity'],update_quantity=cd['update'])
    return redirect('cart_detail')

#remove from cart
def cart_remove(request,craft_id):
    cart=Cart(session)
    craft=get_object_or_404(Craft,id=craft_id)
    cart.remove(craft)
    return redirect('cart_detail')


def cart_detail(request):
    cart=Cart(request)
    return render(request,'cart/detail.html',{"cart":cart})
