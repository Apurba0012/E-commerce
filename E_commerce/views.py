from django.shortcuts import render
from app.models import Category,Products

def master(request):
    return render(request, 'master.html')


def index(request):
    category = Category.objects.all() #all category fetch from database
    product = Products.objects.all()
    context = {
        'category' : category,  #context dict 'category' access through html
        'product'  : product,
    }
    return render(request, 'index.html',context)