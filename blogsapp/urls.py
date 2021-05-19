from django.conf.urls import url
from  blogsapp import views    
urlpatterns = [
  url(r'^$',views.blogview,name='blogsapp')  
]