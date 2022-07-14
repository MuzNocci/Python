from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<div>Olá, este é o meu primeiro site em Django.</div>')