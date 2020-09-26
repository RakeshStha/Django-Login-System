from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect



#password for rakesh is rakehsshrestha
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return redirect("/login")
    return render(request,'index.html')

def loginUser(request):
    if request.method =="POST":
        #check if user has entered correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
    # No backend authenticated the credentials
            return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")