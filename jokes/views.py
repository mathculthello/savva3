from django.shortcuts import render, redirect
from .forms import JokeForm
from .models import Joke
from django.contrib import messages
# Create your views here.

def index(request):
    form=JokeForm()
    jokes=Joke.objects.filter(published=True)
    return render (request, 'jokes/index.html', {'form': form, 'jokes': jokes})


def add(request):
    a=JokeForm(request.POST)
    a.save()
    messages.success(request, 'Спасибо, запись добавлена.')
    return redirect('jokes:index')
