from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Donkey, Health, Aicohol
# Create your views here.

# 창 띄우기
def home(request):
    donkeys = Donkey.objects
    donkey_list = Donkey.objects.all()
    donkey_paginator = Paginator(donkey_list,3)
    donkey_page = request.GET.get('donkey_page')
    donkey_posts = donkey_paginator.get_page(donkey_page)

    return render(request,'home.html',{'donkeys':donkeys,'donkey_posts':donkey_posts})

def health(request):
    healths = Health.objects
    health_list = Health.objects.all()
    health_paginator = Paginator(health_list,3)
    health_page = request.GET.get('health_page')
    health_posts = health_paginator.get_page(health_page)

    return render(request,'health.html',{'healths':healths,'health_posts':health_posts})

def aicohol(request):
    aicohols = Aicohol.objects
    aicohol_list = Aicohol.objects.all()
    aicohol_paginator = Paginator(aicohol_list,3)
    aicohol_page = request.GET.get('aicohol_page')
    aicohol_posts = aicohol_paginator.get_page(aicohol_page)

    return render(request,'aicohol.html',{'aicohols':aicohols,'aicohol_posts':aicohol_posts})

# 디테일창 만들기
def detail_home(request,donkey_id):
    donkeyss = get_object_or_404(Donkey, pk=donkey_id)
    return render(request, 'detail_home.html',{'donkey':donkeyss})

def detail_health(request,health_id):
    healthss = get_object_or_404(Health, pk=health_id)
    return render(request, 'detail_health.html',{'health':healthss})

def detail_aicohol(request,aicohol_id):
    aicoholss = get_object_or_404(Aicohol, pk=aicohol_id)
    return render(request, 'detail_aicohol.html',{'aicohol':aicoholss})

# 새 테이블 만들기

def new_home(request):
    return render(request, 'new_home.html')
    
def new_health(request):
    return render(request, 'new_health.html')

def new_aicohol(request):
    return render(request, 'new_aicohol.html')

# 새창 만들기

def create_home(request):
    donkey = Donkey()
    donkey.title = request.GET['title']
    donkey.body = request.GET['body']
    donkey.pub_date = timezone.datetime.now()
    donkey.name = request.GET['name']
    donkey.save()

    return redirect("board:detail_home", donkey.id)

def create_health(request):
    health = Health()
    health.title = request.GET['title']
    health.body = request.GET['body']
    health.pub_date = timezone.datetime.now()
    health.name = request.GET['name']
    health.save()
    
    return redirect("board:detail_health", health.id)

def create_aicohol(request):
    aicohol = Aicohol()
    aicohol.title = request.GET['title']
    aicohol.body = request.GET['body']
    aicohol.pub_date = timezone.datetime.now()
    aicohol.name = request.GET['name']
    aicohol.save()

    return redirect("board:detail_aicohol", aicohol.id)