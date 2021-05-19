# from django.conf.urls import url
from django.conf.urls import include, url
from django.urls import path
from  eventsapp import views    

urlpatterns = [
 url(r'^$',views.eventview,name='events&parties'),
 url(r'^holi-beach-party$',views.holiview,name='holievents'),
 url(r'^goa-beach-party$',views.beachview,name='goaevents'),
  # path('events/',views.test2),
  # path('',views.test2),
]