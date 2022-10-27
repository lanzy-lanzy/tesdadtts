from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'site/index.html' )
def register(request):
    return render(request, 'site/register.html' )
def login(request):
    return render(request, 'site/login.html' )
def base(request):
    return render(request, 'site/base.html' )
def signup(request):
    return render(request, 'site/signup.html' )
def dashboard(request):
    return render(request, 'site/dashboard.html' )