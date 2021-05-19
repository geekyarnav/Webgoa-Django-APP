from django.conf.urls import url
from  packagesapp import views

urlpatterns = [
  url(r'^about/',views.aboutview,name='about'),  
  url(r'^grouptrips/',views.grouptrips,name='grouptrips'),  
  url(r'^contact/',views.contactview,name='contact'),    
]