from django.contrib import admin
from django.urls import path
from loan import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name="Loan"),
    path('home-loan',views.homeloan,name="Homeloan"),
    path('loan-against-property',views.lap,name="Loanagainstproperty"),
    path('business-loan',views.businessloan,name="Businessloan"),
    path('commercial-loan',views.commercial,name="Commercialloan"),
    path('personal-loan',views.personal,name="Personalloan"),
    path('balance-transfer',views.balancetrn,name="BalanceTransfer"),
    path('secure-and-unsecure-loan',views.secnunsec,name="Secureandunsecureloan"),
]