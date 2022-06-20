from django.shortcuts import render
from .models import ToDoListItem
from django.http import HttpResponseRedirect

def todoappView(request):
    all_todo_items = ToDoListItem.objects.all()
    return render(request,'todolist.html',{'all_items':all_todo_items})



def addTodoView(request):
    x = request.POST['content'] #hello
    new_item = ToDoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')


def deleteTodoView(request,j):
    y= ToDoListItem.objects.get(id=j)
    y.delete()
    return HttpResponseRedirect('/todoapp/')