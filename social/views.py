from django.shortcuts import render

# Create your views here.

def signup(request):
    return render(request, 'social/signup.html')

def login(request):
    return render(request, 'social/login.html')

def social(request):
    return render(request, 'social/social.html')