from django.conf.urls import url
from  hotelsapp import views


urlpatterns = [
  url(r'^$',views.test,name='hotels')  
]