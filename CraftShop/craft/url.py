from django.conf.urls import url
from . import views

urlpatterns=[
url('^$',views.welcome,name="welcome"),
url('^search/',views.search_result,name="search_result")
]
