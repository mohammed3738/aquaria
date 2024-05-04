import email
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def index(request):
    # return HttpResponse("Hello Home")
    return render(request, "home/index.html")
def about(request):
    # return HttpResponse("Hello About")
    return render(request, "home/about.html")

def contact(request):
    # return HttpResponse("Hello Contact")
    if request.method =='POST':
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        text= request.POST['message']
        
        # print(name,email,phone,text)

        if len(name)<2 or len(email)<3 or len(phone)<10:
            messages.error(request,"Please fill the form correctly")
        else:
            contact = Contact(name=name,email=email,phone=phone,text=text)
            contact.save()
            messages.success(request,"Your message is submitted")
            # return redirect (contact)
        
    # 
    return render(request, "home/contact.html")