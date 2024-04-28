from django.shortcuts import render


def index(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


def projects(request):
    return render(request, 'projects.html')
