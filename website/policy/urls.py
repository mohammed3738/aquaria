from django.contrib import admin
from django.urls import path
from policy import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name="Policy"),
    path('health-insurance',views.healthinsurance,name="HealthInsurance"),
    path('life-insurance',views.lifeinsurance,name="LifeInsurance"),
    path('term-insurance',views.terminsurance,name="TermInsurance"),
    path('general-insurance',views.generalinsurance,name="GeneralInsurance"),
    path('business-insurance',views.businessinsurance,name="BusinessInsurance"),
]