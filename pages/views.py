from django.shortcuts import render
from django.http import HttpResponse


def index(requset):
    return render(requset,"index.html")

def about(request):
    return HttpResponse('О нас')

def catsMale(requset):
    return HttpResponse('Коты')

def catsFemale(request):
    return HttpResponse('Кошки')

def litter(request):
    return HttpResponse('Помет')

def gelded(request):
    return HttpResponse('Кострат')

def aboutBreed(request):
    return HttpResponse('О породе')

def contacts(request):
    return HttpResponse('Контакты')
