import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
        {'title' : 'Official Python Tutorial',
         'url'   : 'https://docs.python.org/3/tutorial/'},
        {'title' : 'How to Think like a Computer Scientist',
         'url'   : 'https://www.greenteapress.com/thinkpython/'},
        {'title' : 'Learn Python in 10 Minutes',
         'url'   : 'https://www.korokithakis.net/tutorials/python'}]

    django_pages = [
        {'title' : 'Official Django Tutorial',
         'url'   : 'https://docs.djangoproject.com/en/2.1/intro/tutorials01/'},
        {'title' : 'Django Rocks',
         'url'   : 'https://www.djangorocks.com/'},
        {'title' : 'How to Tango with Django',
         'url'   : 'https://www.tangowithdjango.com/'}]

    other_pages = [
        {'title' : 'Bottle',
         'url'   : 'https://bottlepy.org/docs/dev'},
        {'title' : 'Flask',
         'url'   : 'https://flask.pocoo.prg'}]

    cats = {'Python'           : { 'pages' : python_pages, 'views' : 128, 'likes': 64 },
            'Django'           : { 'pages' : django_pages, 'views' : 64,  'likes': 32 },
            'Other Frameworks' : { 'pages' : other_pages,  'views' : 32,  'likes': 16 } }


    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_page(cat, title, url, views=0):
    # get or create returns a tuple
    # second elem - bool showing whether an object was created or not
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c

# only run population sript if this script is run as standalone
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
