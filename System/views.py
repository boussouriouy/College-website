from django.shortcuts import render
from .models import Destination
# Create your views here.

def home(request):
    dest1 = Destination()
    dest1.img = '2.png'
    dest1.name = 'Labe'
    dest1.desc ='This is one fo the best city'
    dest1.price = 300
    dest1.offer = True
    
    dest3 = Destination()
    dest3.img = '4.png'
    dest3.name = 'Labe'
    dest3.desc ='This is one fo the best city'
    dest3.price = 400
    dest3.offer = False
    
    dest6 = Destination()
    dest6.img = 'me.jpg'
    dest6.name = 'Labe'
    dest6.desc ='This is one fo the best city'
    dest6.price = 500
    dest6.offer = True
    
    dests = [dest1, dest3, dest6 ]
    
    context = {
        'descript': dests
    }
    return render(request, 'main.html', context)

def info(request):
    context = {
        'title':'<h3>Info System</h3>'
    }
    return render(request, 'info.html', context)

def about(request):
    context = {
        'title':'<h3>About System</h3>'
    }
    return render(request, 'about.html', context)
