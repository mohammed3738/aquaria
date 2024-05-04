from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Hello Policy")
    return render(request,"insurance/insurance.html") 

def healthinsurance(request):
    # return HttpResponse("Health Ins")
    return render(request,"insurance/healthinsurance.html")

def lifeinsurance(request):
    # return HttpResponse("lifeinsurance")
    return render(request,"insurance/lifeinsurance.html")    

def terminsurance(request):
    # return HttpResponse("terminsurance")
    return render(request,"insurance/terminsurance.html")

def generalinsurance(request):
    # return HttpResponse("generalinsurance")
    return render(request,"insurance/generalinsurance.html")

def businessinsurance(request):
    # return HttpResponse("businessinsurance")
    return render(request,"insurance/businessinsurance.html")

