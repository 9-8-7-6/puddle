from django.shortcuts import render,redirect
from django.contrib.auth import logout as auth_logout
from item.models import Category, Item
from django.contrib import messages 
from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })
    
def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    
    return render(request, 'core/signup.html',{
         'form': form
    })

def logout(request):
	auth_logout(request)
	messages.success(request,('Youre now logged out'))
	return redirect('/')