from django.shortcuts import render
from .models import  Artical as ar
from django.http import HttpResponse

# Create your views here.
def artical_list(request):
    artical = ar.objects.all()
    
    return render(request,'articals/artical_list.html',{'artical': artical})
def artical_details(request,slug):
    #return   HttpResponse(slug)
    artical = ar.objects.get(slug=slug)
    return render(request,'articals/artical_detail.html',{'artical': artical})