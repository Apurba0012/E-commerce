from django.shortcuts import render
from app.models import Category

def master(request):
    return render(request, 'master.html')


def index(request):
    category = Category.objects.all() #all category fetch from database

    context = {
        'category' : category  #context dict 'category' access through html
    }
    return render(request, 'index.html',context)