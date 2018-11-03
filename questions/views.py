from django.shortcuts import render, redirect
from .forms import QuestionForm
from django.contrib import messages
from django.core.mail import mail_managers

# Create your views here.

def add(request):
    a=QuestionForm(request.POST)
    try:
        obj=a.save()
        mail_managers('Новый вопрос:'+obj.theme,obj.text)
        messages.success(request, 'Спасибо, вопрос добавлен.')
    except:
        messages.error(request, 'Ошибка добавления.')

    return redirect('index')
