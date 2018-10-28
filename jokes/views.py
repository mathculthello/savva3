from django.shortcuts import render, redirect
from .forms import JokeForm
from django.contrib import messages
# Create your views here.

def index(request):
    form=JokeForm()
    return render (request, 'jokes/index.html', {'form': form})


def add(request):
    a=JokeForm(request.POST)
    a.save()
    messages.success(request, 'Спасибо, запись добавлена.')
    return redirect('jokes:index')
