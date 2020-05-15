from django.shortcuts import render, redirect
from django.contrib import messages    
from django.contrib.auth.models import User, auth

# Create your views here.


def register(request):
    if request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['password1']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken Please try something else')
                return redirect(".")
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken Please try something else')
                return redirect(".")
            else:
                user = User.objects.create_user(username= username, password=password, email=email, first_name=first_name, last_name=last_name )
                user.save();
                messages.info(request, 'Registred you can login! ' + str(user))
                return redirect('go_in')  
            
        else:
            messages.info(request, 'Password does not match Please try again')
            return redirect(".")
        
    else:
       return render(request, 'sign.html')


def go_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/System/main')
        else:
            messages.info(request, 'Invalid credentials '+ str(username)+ ' Try again')
            return redirect('.')
       
    else:
      return render(request, 'login.html')



def main(request):
    
    return render(request, 'acount_index.html')

# def go_out(request):
#     auth.logout(request)
#     return redirect('main') 