from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'pages/index.html')

def page(request, page):
    template='pages/'+page+'.html'
    
    return render (request, template)
