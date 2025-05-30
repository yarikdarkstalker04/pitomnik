from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"pages/about.html")

def catsMale(request):
    return render(request, "pages/catsMale.html")

def catsFemale(request):
    return render(request, "pages/catsFemale.html")

def litter(request):
    return render(request,"pages/litter.html")

def gelded(request):
    return render(request,"pages/gelded.html")

def aboutBreed(request):
    return render(request,"pages/aboutBreed.html")

def contacts(request):
    return render(request,"pages/contacts.html")
