import math
from django.shortcuts import render, redirect
from .forms import JokeForm
from .models import Joke
from django.contrib import messages
from django.core.mail import mail_managers

PAGE_SIZE = 12

def get_order(request):
    str_sort = request.GET.get('sort', 'byDate').lower()
    order = ('-date_added',)

    if (str_sort == "byrating"):
        order = ('-rating', '-date_added')
    
    return order


def get_pages_count(query_dict):
    return math.ceil(Joke.objects.filter( **query_dict ).count() / PAGE_SIZE)

def get_current_page(query_dict, order_by, page):
    jokes = Joke.objects \
        .filter( **query_dict ) \
        .order_by( *order_by ) \
        [(page - 1) * PAGE_SIZE: page * PAGE_SIZE]

    return jokes

def get_page(request):
    str_page = request.GET.get('page', '')
    try:
        page = int(str_page)
    except:
        page = 1
    
    return page

def index(request):
    query_dict = {
        "published": True, 
        "adult": False,
    }
    current_page = get_page(request)
    order_by = get_order(request)
    pages_count = get_pages_count(query_dict)
    jokes = get_current_page(
        query_dict=query_dict, 
        order_by=tuple(order_by), 
        page=current_page,
    )
    
    return index_all(request, jokes, {
        "current": current_page,
        "count": pages_count,
        "size": PAGE_SIZE
    })

def yo(request):
    query_dict = {
        "published": True, 
        "adult": True,
    }
    current_page = get_page(request)
    order_by = get_order(request)
    pages_count = get_pages_count(query_dict)
    jokes = get_current_page(
        query_dict=query_dict, 
        order_by=order_by, 
        page=current_page,
    )

    return index_all(request, jokes, {
        "current": current_page,
        "count": pages_count,
        "size": PAGE_SIZE
    })

def index_all(request, jokes, pagination={}):
    form=JokeForm()
    meta = {
        'keywords': [
            'анекдоты', 
            'математические анекдоты', 
            'шутки', 
            'сборник анекдотов', 
            'Савватеев шутит', 
            'коллекция анекдотов'
        ],
        'description': 'Сборник математических анекдотов, присылаемых читателями.'
    }

    return render (request, 'jokes/index.html', {'form': form, 'jokes': jokes, 'pagination': pagination})

def add(request):
    a=JokeForm(request.POST)
    obj=a.save()
    mail_managers('Новый анекдот:'+obj.title,obj.text)
    messages.success(request, 'Спасибо, запись добавлена.')
    return redirect('jokes:index')
