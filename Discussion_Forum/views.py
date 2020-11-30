from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import * 
from .forms import * 
# Create your views here.
 
def index(request):
    return render(request,'index.html')

def main(request):
    return render(request,'main.html')

def box_one(request):
    return render(request,'box_one.html')

def box_two(request):
    return render(request,'box_two.html')

def box_three(request):
    return render(request,'box_three.html')

def about(request):
    return render(request,'about.html')

def home(request):
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
 
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request,'home.html',context)
 
def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/home')
    context ={'form':form}
    return render(request,'addInForum.html',context)
 
def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/home')
    context ={'form':form}
    return render(request,'addInDiscussion.html',context)