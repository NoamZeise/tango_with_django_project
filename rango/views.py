from django.shortcuts import render


def index(request):
    # match template in index.html
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # render fills in templates using the dict
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    # render fills in templates using the dict
    return render(request, 'rango/about.html')
