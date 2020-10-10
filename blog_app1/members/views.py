from django.shortcuts import render , redirect
from django.views import generic
# Create your views here.
from django.contrib.auth.models import User , auth
from django.urls import reverse_lazy
from django.contrib.auth import logout, authenticate, login

def register(reqests):
    if reqests.method == 'POST':
        first_name = reqests.POST.get('first_name')
        print(type(first_name))
        last_name = reqests.POST.get('last_name')
        username = reqests.POST.get('user_name')
        email = reqests.POST.get('eamil')
        password = reqests.POST.get('password1')
        password2 = reqests.POST.get('password')
        if (first_name and last_name and username and email and password2 and password2) == '':
            return render(reqests , 'registration/register.html' , {'fail' : 'fields cannot be empty'})
        else:
            if password == password2:
                if User.objects.filter(username = username).exists():
                    return render(reqests , 'registration/register.html' , {'fail' : 'username taken'})
                elif User.objects.filter(email = email).exists():
                    return render(reqests , 'registration/register.html' , {'fail' : 'eamil taken'})
                First_name = first_name.capitalize()
                Last_name = last_name.capitalize()
                user = User.objects.create_user(username = username , password =  password , first_name =  First_name , last_name = Last_name , email=email)
                user.save()
            else:
                return render(reqests , 'registration/register.html' , {'fail' : 'password miss match'})
            print('it worked')
            return redirect('login')
    return render(reqests , 'registration/register.html')
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'registration/login.html')

    return render(request, 'registration/login.html')
def logoutUser(requests):
    logout(requests)
    return redirect("login")