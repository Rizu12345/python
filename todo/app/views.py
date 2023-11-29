from django.shortcuts import render
from .models import*
from .forms import *
# Create your views here.

def index(request):
    context={}

    todo=Todo.objects.all()
    todo_form=Todo_form()

    context['todo']=todo
    context['todo_form']=todo_form
    return render(request,'index.html',context)

