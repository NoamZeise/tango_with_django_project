from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # match template in index.html
    context_dict = { 'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!' }
    # render fills in templates using the dict
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
