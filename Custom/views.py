from django.shortcuts import render

from .models  import Customer
# Create your views here.

def table(request):
    destes = Customer.objects.all()
    context = {
        'descript': destes
    }
    return render(request, 'index.html', context)

# def detail(request, pk):
#     obj = Customer.objects.get(Customer, pk)
    
#     context = {
#         'object': obj
#     }
#     return render(request, 'detail.html', context)