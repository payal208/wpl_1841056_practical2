from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello, This is Payal Wakekar from T3 Batch and my PRN is 1841054!@.</h1>')
