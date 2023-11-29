from django.shortcuts import render
from .models import*
from .forms import *
# Create your views here.

def index(request):
    context={}

    todo=Todo.objects.all()
    todo_form=Todo_form()


    if request.method=="POST":
        if 'save' in request.POST:
            
         todo_form=Todo_form(request.POST)
         todo_form.save()

        elif 'delete' in request.POST:
           key=request.POST.get('delete')
           todo_del=Todo.objects.get(id=key)
           todo_del.delete()
           
        


    context['todo']=todo
    context['todo_form']=todo_form
    return render(request,'index.html',context)

   