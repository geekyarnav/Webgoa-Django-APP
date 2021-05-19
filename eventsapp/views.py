from django.shortcuts import render
from django.http import HttpResponse 
# ---------MTV---------
# 1 import models that we used
from .models import HoliDetail,BeachDetail

#  Create your views here.
# def index(request):
#     return render(request,'eventsapp/templates/beachparty.html')
def eventview(request):
    template_name= '../templates/event.html'
    context={}
    return render(request,template_name,context)  

def holiview(request):
    # 2 use the view to query the model for data that we will need
    # obj = HoliDetail.objects.get(id=3)
    obj = HoliDetail.objects.all()
    # obj_detail = PackageDetail.objects.all
    # obj_type = PackageType.objects.all
    template_name= '../templates/holiparty.html'
    # template_name= '../templates/newholi.html'
    context={"object": obj  }  #    "type": obj_type,
                # "detail":obj_detail
    return render(request,template_name,context)
    # return render(request,'../templates/holiparty.html')

def beachview(request):
    # 2 use the view to query the model for data that we will need
    # obj = HoliDetail.objects.get(id=3)
    obj = BeachDetail.objects.all()

    template_name= '../templates/beachparty.html'
    context={"object": obj}
    return render(request,template_name,context)    
