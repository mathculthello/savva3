from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'pages/index.html')

def page(request, page):
    return render (request, 'pages/'+page+'.html')
