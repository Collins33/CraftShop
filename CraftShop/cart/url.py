from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
url('^$',views.cart_detail,name="cart_detail"),
url(r'^add/(?P<craft_id>\d+)/$',views.cart_add,name='cart_add'),
url(r'^remove/(?P<craft_id>\d+)/$',views.cart_remove,name='cart_remove'),]
