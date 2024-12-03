from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post
from django.http import Http404
# Create your views here.
# 
# posts = [
#         {'id':1,'title':'post 1','content':'content of post 1'},
#         {'id':2,'title':'post 2','content':'content of post 2'},
#         {'id':3,'title':'post 3','content':'content of post 3'},
#         {'id':4,'title':'post 4','content':'content of post 4'}
#     ]
def index(request):
    blog_title = 'karun Posts'
    posts = Post.objects.all()

    return render(request,"blog/index.html",{'blog_title': blog_title,'posts':posts})

def detail(request,slug):
    # post = next((item for item in Post if item['id'] == post_id),None)
    # logger = logging.getLogger("TESTING")
    # logger.debug(f"post varriable is {post}")
    try:
       posts = Post.objects.get(slug=slug)
    except Exception:
         raise Http404("page doesnot exist")
    return render(request,"blog/detail.html",{'post':posts})

def old_url_detail(request):
    return redirect(reverse('blogapp:new_page_url'))

def new_url_detail(request):
    return HttpResponse("this is new url page")