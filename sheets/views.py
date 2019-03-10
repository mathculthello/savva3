from django.shortcuts import render
from django.db import connection
from .models import Sheet

def index(request):
    sheet_list = Sheet.objects.all()
    context = {'sheets': sheet_list}
    return render(request, 'sheets/sheets.html', context)
