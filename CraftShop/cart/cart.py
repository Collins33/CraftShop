from decimal import Decimal
from django.conf import settings
from craft.models import Craft,categories

#Create the cart class to manage the cart
class Craft(object):
    def __init__(self,request):
        #store current session
        self.session=request.session
        #try to get the cart from the current session
        cart=self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #if the cart is not in the session,add it as an empty dictionary
            cart=self.session[settings.CART_SESSION_ID]={}
        self.cart=cart
