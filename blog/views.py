from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from .models import Post


def blog(request) : 
    posts = Post.objects.all()

    return render(request,'blog/blog.html',{"posts":posts})

def todo(request) :
    return render(request,'blog/todo.html')


def post_detail(request,num) :
    post=Post.objects.get(pk=num)
    return render(request,"blog/blog_detail.html",{'post':post})


