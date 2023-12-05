from django.shortcuts import render
# from django.contrib.auth.decorator import login_required

# Create your views here.
def home(request):
    return render(request, "home.html")

def profil(request):
    return render(request, "profil.html", {"user" : None})

def login(request):
    return render(request, "login.html")

def logout(request):
    return render(request, "logout.html")

def header(request):
    return render(request, "header.html")

# @login_required 
def dashboard(request): #Main srceen 
    return render(request, 'templates/profil.html' , {'section' : 'profil'})
    
