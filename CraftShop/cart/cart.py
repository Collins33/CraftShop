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

    #this method adds to cart and saves cart
    def add(self,craft,quantity=1,update_quantity=False):
        #get the craft id
        craft_id=str(craft.id)
        #use craft id to check if the craft is in the session:
        if craft_id not in self.craft:
            #if not add the craft to the cart
            #the key is the craft id
            self.cart[craft_id]={'quantity':0,'price':str(craft.craft_price)}

        if update_quantity:
            self.cart[craft_id]['quantity']=quantity
        else:
            self.cart[craft_id]['quantity']=+quantity

        self.save()

     #this method saves the changes to the cart
     def save(self):
         #update the session
         self.session[settings.CART_SESSION_ID]=self.cart
         #mark it as modified so that django can save it
         self.session.modified=True


    #remove from the cart
    def remove(self,craft):
        #get the craft id
        craft_id=str(craft.id)
        if craft_id in self.cart:
            del self.cart[craft_id]
            #update the session after deleting
            self.save()

    #iterate over items in the cart and get them from the database
    def __iter__(self):
        craft_ids=self.cart.keys()

        #get crafts from the database
        crafts=Craft.objects.filter(id__in=craft_ids)
        #add them to the cart
        for craft in crafts:
            self.cart[str(craft.id)]['craft']=craft

        #iterate over the items in the cart
        for item in self.cart.values():
            item['price']=Decimal(item['price'])
            item['total_price']=item['price'] * item['quantity']
            yield item

    #get the total number of items in the cart
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())    
