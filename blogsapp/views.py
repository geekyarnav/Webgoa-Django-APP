from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blogview(request):
    # return HttpResponse("blogapp")
    template_name= '../templates/blogs.html'
    # context={"object": obj}
    return render(request,template_name)