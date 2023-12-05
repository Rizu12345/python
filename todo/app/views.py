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
            key=request.POST.get('save')

            if not key:
              todo_form=Todo_form(request.POST)
            else:
              todo_edit=Todo.objects.get(id=key)
              todo_form=Todo_form(request.POST,instance=todo_edit)

            todo_form.save()
            todo_form=Todo_form()
           
        elif 'delete' in request.POST:
           key=request.POST.get('delete')
           todo_del=Todo.objects.get(id=key) 
           todo_del.delete()


        elif 'edit' in request.POST:
           key=request.POST.get('edit')
           todo_edit=Todo.objects.get(id=key)
           todo_form=Todo_form(instance=todo_edit)


           
        


    context['todo']=todo
    context['todo_form']=todo_form
    return render(request,'index.html',context)

   