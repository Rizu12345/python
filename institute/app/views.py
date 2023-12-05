from django.shortcuts import render
from . models import *
# Create your views here.
def index(request):
    obj=Institute.objects.all()
    return render(request,'index.html',{'obj':obj})