from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name="Home"),
    path('about',views.about,name="About"),
    path('contact',views.contact,name="Contact"),
]