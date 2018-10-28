from django.shortcuts import render, redirect
from .forms import JokeForm
from .models import Joke
from django.contrib import messages
# Create your views here.

def index(request):
    jokes=Joke.objects.filter(published=True)
    return index_all(request, jokes)

def yo(request):
    jokes=Joke.objects.filter(published=True,adult=True)
    return index_all(request, jokes)

def index_all(request, jokes):
    form=JokeForm()
    return render (request, 'jokes/index.html', {'form': form, 'jokes': jokes})

def add(request):
    a=JokeForm(request.POST)
    a.save()
    messages.success(request, 'Спасибо, запись добавлена.')
    return redirect('jokes:index')
