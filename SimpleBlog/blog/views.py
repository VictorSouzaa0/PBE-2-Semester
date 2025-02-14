from django.shortcuts import render
from .models import Postt
# Create your views here.

def listen_posts(request):
    posts = Postt.objects.all().order_by('creation_date')
    return render(request,'listen_posts.html',{'posts': posts})
