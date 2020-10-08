
from django.shortcuts import render 

def home(request):
    #return HttpResponse("this is homepage")
    return render(request,'homepage.html')

def about(request):
    #return HttpResponse("thi aassdsds is about Request")
    return render(request,'about.html')