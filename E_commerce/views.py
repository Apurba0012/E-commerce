from django.shortcuts import render,redirect
from app.models import Category,Products

from django.contrib.auth import authenticate,login
from app.models import UserCreateForm

def master(request):
    return render(request, 'master.html')


def index(request):
    category = Category.objects.all() #all category fetch from database
    categoryID = request.GET.get('category')
    if categoryID:
        product = Products.objects.filter(sub_category =categoryID)
    else:
        product = Products.objects.all()
    context = {
        'category' : category,  #context dict 'category' access through html
        'product'  : product,
    }
    return render(request, 'index.html',context)


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],

            )
            login(request,new_user)
            return redirect('index')
    else:
        form = UserCreateForm()

    context = {
        'form':form,
    }
    return render(request,'registration/signup.html',context)
