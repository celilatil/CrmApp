from django.shortcuts import render 

def index(request):
    return render(request, 'core/base.html')

def about(request):
    return render(request, 'core/about.html')