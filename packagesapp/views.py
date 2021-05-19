from django.shortcuts import render
from django.http import HttpResponse 
# ---------MTV---------
# 1 import models that we used
from .models import PackageDetail,PackageType

def homeview(request):
    # return HttpResponse("packagesapp")
    return render(request,'../templates/home.html',context={})
    
def aboutview(request):
    # return HttpResponse("packagesapp")
    return render(request,'../templates/about.html',context={})
    
def contactview(request):
    # return HttpResponse("packagesapp")
    return render(request,'../templates/contact.html',context={})

def grouptrips(request):
    # 2 use the view to query the model for data that we will need
    # obj = HoliDetail.objects.get(id=3)
    obj = PackageDetail.objects.all()
    obj = PackageType.objects.all()

    template_name= '../templates/grouptrip.html'
    context={"object": obj}
    return render(request,template_name,context)        


