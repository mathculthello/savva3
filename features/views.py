from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import mail_managers

from .forms import FormulaeForm
# Create your views here.
def formulae_add(request):
    a=FormulaeForm(request.POST)
    try:
        obj=a.save()
        mail_managers('Формула', obj.formulae)
        messages.success(request, 'Спасибо :)')
    except:
        messages.error(request, 'Ошибка добавления.')

    return redirect('index')
