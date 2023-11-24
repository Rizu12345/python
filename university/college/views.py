from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>welcome to university</h1>')
def about(request):
    return HttpResponse('<h2>about us</h2>')
def package(request):
    return HttpResponse('<h1>packages</h1>')
def colleges(request):
    return HttpResponse('<h1>calm</h1>')