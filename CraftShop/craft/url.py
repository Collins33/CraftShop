from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
url('^$',views.welcome,name="welcome"),
url(r'^search/', views.search_result, name="search_result"),
url(r'^craft/(\d+)',views.craft,name ='crafts'),
url(r'^all/',views.all_craft,name="allCraft"),
url(r'^new/crafts',views.new_craft,name="newCraft"),

url(r'^ajax/newsletter/$',views.newsLetter,name="newsletter")
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
