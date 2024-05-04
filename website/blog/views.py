from email import message
from django.contrib import messages
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.
def blog(request):
    # return HttpResponse("Hello Blog")
    allPosts= Post.objects.all()

    context={'allPosts':allPosts}

    return render(request,'blog/blog.html',context)



def blogPost(request,slug):
    # return HttpResponse(f"Hello Blog:{slug}")
    post=Post.objects.filter(slug=slug)
    if post==None:
        context={'post':post}
        return render (request,'blog/blog.html',context)
    else:
        context={'post':post}
        return render(request,'blog/blogpost.html',context)

def search(request):
    # return HttpResponse("Search Page")
    # allPosts=Post.objects.all()
    query=request.GET['search']
    if len(query)>60:
        allPosts = Post.objects.none()
    else:
        allPostst=Post.objects.filter(title__icontains=query)
        allPostsc=Post.objects.filter(content__icontains=query)
        allPosts=allPostst.union(allPostsc)
    if allPosts.count()== 0:
        messages.warning(request,"Kindly make a relevant search")
    params={'allPosts':allPosts, 'query':query}
    return render(request,'blog/search.html',params)        