from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login
from .models import Blog
from .forms import NewBlogForm
import datetime as dt


# Create your views here.
def welcome(request):
    date = dt.date.today()
    
    return render(request, 'welcome.html', {"date": date})

def about(request):
    return render(request, 'about.html')

def program(request):
    return render(request, 'program.html')

def sermon(request):
    return render(request, 'sermon.html')

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {"blog": blog})

def contact(request):
    return render(request, 'contact.html')

def search_results(request):
    if 'blog' in request.GET and request.GET["blog"]:
        search_term = request.GET.get("blog")
        searched_blogs = Blog.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"blogs": searched_blogs})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
