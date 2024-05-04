from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.blog,name="Blog"),
    path('search',views.search ,name="Search"),
    path('<str:slug>',views.blogPost,name="BlogPost"),
]