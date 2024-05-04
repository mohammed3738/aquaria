from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse("Hello Loan")
    return render(request,"loan/loan.html")

def homeloan(request):
    # return HttpResponse("Home Loan")
    return render(request,"loan/homeloan.html")    

def lap(request):
    # return HttpResponse("Loan Against property")
    return render(request,"loan/loanagainstproperty.html")

def businessloan(request):
    # return HttpResponse("Business Loan")
    return render(request,"loan/businessloan.html")

def commercial(request):
    # return HttpResponse("Commercial Loan")
    return render(request,"loan/commercialloan.html")

def personal(request):
    # return HttpResponse("Personal Loan")
    return render(request,"loan/personalloan.html")

def balancetrn(request):
    # return HttpResponse("Balance Transfer")
    return render(request,"loan/balancetransfer.html")

def secnunsec(request):
    # return HttpResponse("Secure and Unsecure Loan")
    return render(request,"loan/secureandunsecureloan.html")