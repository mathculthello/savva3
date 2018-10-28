from django.shortcuts import render, redirect
from .forms import JokeForm
from .models import Joke
from django.contrib import messages
from django.core.mail import mail_managers
# Create your views here.

def index(request):
    jokes=Joke.objects.filter(published=True,adult=False)
    return index_all(request, jokes)

def yo(request):
    jokes=Joke.objects.filter(published=True,adult=True)
    return index_all(request, jokes)

def index_all(request, jokes):
    form=JokeForm()
    return render (request, 'jokes/index.html', {'form': form, 'jokes': jokes})

def add(request):
    a=JokeForm(request.POST)
    obj=a.save()
    mail_managers('Новый анекдот:'+obj.title,obj.text)
    messages.success(request, 'Спасибо, запись добавлена.')
    return redirect('jokes:index')
